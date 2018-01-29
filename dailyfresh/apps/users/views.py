from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse
# 用于对用户id进行加密解密
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
from django.conf import settings
# 用于发送邮件
from django.core.mail import send_mail
from .models import *
from django.contrib.auth import authenticate, login, logout
from celery_takes.takes import send_email
import re
# 导入用于判断是否已登录的装饰器
from django.contrib.auth.decorators import login_required
from redis import StrictRedis
from django_redis import get_redis_connection
from apps.goods.models import *
from apps.orders.models import *


# class ReAsView(View):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         a = super(ReAsView, cls).as_view(**initkwargs)
#
#         return login_required(a)


class ReAsView(object):
    """自定义类用于重写as_view方法"""
    @classmethod
    def as_view(cls, **initkwargs):
        a = super(ReAsView, cls).as_view(**initkwargs)

        return login_required(a)


# Create your views here.
class Register(View):
    """注册视图"""

    def get(self, request):
        """get方式请求返回注册页面"""
        return render(request, 'users/register.html')

    def post(self, request):
        """post方式请求"""

        # 获取表单提交的数据
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        # print(1)
        # 如果有数据为空返回错误信息
        if not all([username, pwd, email]):
            return render(request, 'users/register.html', {'res': '注册信息有误'})
        # 如果邮箱地址不匹配返回错误信息
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):

            return render(request, 'users/register.html', {'res': '邮箱格式错误'})

        try:
            # 验证用户名是否已经注册过
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 如果未通过get方法查询到会抛出异常,捕获异常并将user的值设置为空
            user = None

        if user:
            # 如果user不为空则用户名已存在
            return render(request, 'users/register.html', {'res': '用户名已存在'})
        # django内置用户模块的create_user方法可以直接创建用户并将信息插入数据库
        user = User.objects.create_user(username, email, pwd)
        # django会默认讲is_active设置为1,1表示已激活
        user.is_active = 0
        user.save()

        # 创建加密对象,过期时间未3600s
        seria = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 3600)

        dict1 = {
            'user_id': user.id
        }
        # 用dumps方法将字典进行加密
        encrypt_user_id = seria.dumps(dict1)
        # 加密后是bytes类型,将bytes进行解码
        encrypt_user_id = encrypt_user_id.decode()

        # 利用celery异步发送邮件
        # send_email.delay(email,username,encrypt_user_id)

        # 邮件标题
        subject = '天天生鲜'
        # 邮件常规内容
        message = ''
        # 发件人
        sender = settings.EMAIL_FROM
        # 收件人列表
        receiver = [email]
        # 邮件内容 html格式
        html_msg = """
            <h1>%s,欢迎您成为天天生鲜注册会员</h1>
            请点击以下链接激活您的账户<br/>
        <a href="http://127.0.0.1:8000/users/active/%s">http://127.0.0.1:8000/users/active/%s</a>
        """ % (user.username, encrypt_user_id, encrypt_user_id)
        # 发送邮件
        send_mail(subject, message, sender, receiver, html_message=html_msg)

        return redirect(reverse('users:login'))


class Active(View):
    """激活链接"""

    def get(self, request, token):
        # 创建加密对象
        seria = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 3600)
        #
        try:
            # 将url提取的参数进行解密
            user_id = seria.loads(token)
            # 从数据库中查找到指定id的账户,讲is_active设置为1表示激活
            user = User.objects.get(id=user_id['user_id'])
            user.is_active = 1
            user.save()
            return redirect(reverse('users:login'))
        except SignatureExpired as e:
            # 如果报错表示链接过期
            return HttpResponse('<h1>链接已过期</h1>')


class Login(View):
    """登录视图"""

    def get(self, request):
        """通过get方式请求"""

        # 如果username在cookie字典当中表示用户勾选了记住账户
        if 'username' in request.COOKIES:
            # 获取用户的用户名
            username = request.COOKIES.get('username')
            # 当记住用户名被勾选时会 增加一个checked
            checked = 'checked'
        else:
            username = ''
            checked = ''

        return render(request, 'users/login.html', {'username': username, 'checked': checked})

    def post(self, request):
        """post方式请求"""

        # 接收用户提交的表单数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 如果有空数据提交返回错误信息
        if not all([username, password]):
            return render(request, 'users/login.html', {'res': '用户名密码不能为空'})

        # django用户模块中内置方法 用来判断账号密码是与数据库匹配,如果匹配到返回用户对象
        # 否则返回空
        user = authenticate(username=username, password=password)
        # 如果user不为空
        if user is not None:
            # 如果用户已经激活
            if user.is_active:
                # 记住登录状态
                login(request, user)
                # print(1)
                url = request.GET.get('next', reverse('goods:index'))

                # 跳转到首页
                response = redirect(url)
                # 如果用户勾选了记住账户,设置cookie值,否则删除cookie的值
                if request.POST.get('remember') == 'on':
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:

                    response.delete_cookie('username')

                return response

            else:
                # 如果未激活返回错误信息
                return render(request, 'users/login.html', {'res': '账户未激活'})
        else:
            # 如果用户名密码验证失败返回错误信息
            return render(request, 'users/login.html', {'res': '用户名密码不正确'})


class Logout(View):
    """退出登录"""

    def get(self, request):
        # djang用户内置方法,退出登录
        logout(request)

        return redirect(reverse('goods:index'))


class UserCenterInfo(ReAsView, View):
    """用户中心的个人中心页面"""
    def get(self, request):
        # 获取登录的user对象
        user = request.user
        # 通过自定义管理器定义的方法获取默认显示的地址对象
        addr = Address.objects.show_def_addr(user)
        # 通过redis模块里的 StrictRedis 创建对象后可直接操作redis数据库
        con = StrictRedis(host='127.0.0.1',port='6379',db=11)
        # 通过django_redis 里的get_redis_connection方法也可以直接操作数据库,同上
        # con = get_redis_connection('default')
        # 拼接出redis数据库中存放的列表key
        history_key = 'history_' + str(user.id)
        # 取出列表里的前五个数据,列表内存放的为用户浏览的商品sku id
        skus_id = con.lrange(history_key, 0, 4)
        # 获取用户浏览过的所有商品的查询集
        skus = GoodsSku.objects.filter(id__in=skus_id)
        # 定义空列表
        sku_list = []

        # 循环遍历从数据库中取出的列表
        for sku_id in skus_id:
            # 循环遍历查询出的对应商品sku对象
            for sku in skus:
                # 当两个值相等时将对象添加至列表中(为保证查询到的数据按顺序存放)
                if sku.id == int(sku_id):
                    sku_list.append(sku)

        # print(sku_list)

        return render(request, 'users/user_center_info.html', {'res': 'info', 'addr': addr, 'sku_list': sku_list})


class UserCenterOrder(ReAsView, View):
    """用户中心订单页面"""
    def get(self, request,page):

        user = request.user
        # 获取当前用户的所有订单信息
        orders = Order_mes.objects.filter(user_id=user).order_by('-create_time')
        # 便利所有订单
        for order in orders:
            # 获取订单对应的订单商品信息
            order_goods = OrderGoods.objects.filter(order_mes_id=order).order_by('-create_time')
            # 便利商品订单信息
            for order_sku in order_goods:
                # 向类中增加属性小计,方便给模板使用
                order_sku.samll_price = order_sku.goods_price * order_sku.goods_count
            # 向类中增加属性,支付状态对应的文字
            order.pay_state_str = order.pay_state_dict[order.pay_state]

            order.order_skus = order_goods

        # 导入分页类
        from django.core.paginator import Paginator
        # 每页显示两条数据
        paginat = Paginator(orders,1)

        page = int(page)
        if page > paginat.num_pages:
            page = 1
        # 当分页总数小于4时,返回的页码为1到总页码+1
        if paginat.num_pages < 5:
            page_list = range(1, paginat.num_pages + 1)
        # 当用户访问的页码小于3时返回前4页
        elif page <= 3:
            page_list = range(1, 6)
        # 当总页码减用户访问的页码小于等于2时,返回 总页码减3到总页码加1的列表
        elif (paginat.num_pages - page) <= 2:
            page_list = range(paginat.num_pages - 4, paginat.num_pages + 1)
        # 否则返回当前页-2到当前页+2的页码
        else:
            page_list = range(page - 3, page + 2)

        # 获取page页的数据
        page_datas = paginat.page(page)

        context = {
            'page_datas':page_datas,
            'page_list':page_list,
            'res': 'order'
        }



        return render(request, 'users/user_center_order.html', context)


class UserCenterSite(ReAsView, View):
    """用户中心收货地址页面"""
    def get(self, request):
        # 获取当前用户对象
        user = request.user
        # 通过自定义的管理器方法,查询是否有默认地址
        # address = Address.objects.show_def_addr(user)
        address = Address.objects.filter(User_id=user)

        return render(request, 'users/user_center_site.html', {'res': 'site', 'address': address})

    def post(self, request):
        # 获取当前用户对象
        user = request.user
        # 获取表单提交的数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zop_code')
        phone = request.POST.get('phone')
        # 判断是否有空数据
        if not all([receiver, addr, phone]):
            return render(request, 'users/user_center_site.html', {'res': '信息不完整'})
        # 如果数据库中已经有了默认地址则将新添加的地址设置为非默认
        if Address.objects.show_def_addr(user):

            is_default = False
        else:
            is_default = True
        # 向数据库中插入地址
        Address.objects.create(User_id=user, receiver=receiver, addr=addr,
                               zip_code=zip_code,
                               phone=phone, is_default=is_default)

        return redirect(reverse('users:site'))
