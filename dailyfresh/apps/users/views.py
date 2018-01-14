from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse
# 用于对用户id进行加密解密
from itsdangerous import TimedJSONWebSignatureSerializer,SignatureExpired
from django.conf import settings
# 用于发送邮件
from django.core.mail import send_mail
from .models import *
from django.contrib.auth import authenticate,login,logout
from celery_takes.takes import send_email
import re


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
            print(3)
            return render(request, 'users/register.html', {'res': '邮箱格式错误'})

        try:
            # 验证用户名是否已经注册过
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 如果未通过get方法查询到会抛出异常,捕获异常并将user的值设置为空
            user=None

        if user:
            # 如果user不为空则用户名已存在
            return render(request, 'users/register.html', {'res': '用户名已存在'})
        # django内置用户模块的create_user方法可以直接创建用户并将信息插入数据库
        user = User.objects.create_user(username, email, pwd)
        # django会默认讲is_active设置为1,1表示已激活
        user.is_active = 0
        user.save()



        # 创建加密对象,过期时间未3600s
        seria = TimedJSONWebSignatureSerializer(settings.SECRET_KEY,3600)

        dict1 = {
            'user_id':user.id
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
        """ %(user.username,encrypt_user_id,encrypt_user_id)
        # 发送邮件
        send_mail(subject, message, sender, receiver,html_message=html_msg)

        return redirect(reverse('users:login'))


class Active(View):
    """激活链接"""
    def get(self,request,token):
        # 创建加密对象
        seria = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 3600)
        #
        try:
            # 将url提取的参数进行解密
            user_id = seria.loads(token)
            # 从数据库中查找到制定id的账户,讲is_active设置为1表示激活
            user = User.objects.get(id=user_id['user_id'])
            user.is_active=1
            user.save()
            return redirect(reverse('users:login'))
        except SignatureExpired as e:
            # 如果报错表示链接过期
            return HttpResponse('<h1>链接已过期</h1>')

class Login(View):
    """登录视图"""
    def get(self,request):
        """通过get方式请求"""

        # 如果username在cookie字典当中表示用户勾选了记住账户
        if 'username' in request.COOKIES:
            # 获取用户的用户名
            username = request.COOKIES.get('username')
            # 当记住用户名被勾选时会 增加一个checked
            checked = 'checked'
        else:
            username = ''
            checked=''

        return render(request,'users/login.html',{'username':username,'checked':checked})

    def post(self,request):
        """post方式请求"""

        # 接收用户提交的表单数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 如果有空数据提交返回错误信息
        if not all([username,password]):

            return render(request, 'users/login.html',{'res':'用户名密码不能为空'})

        # django用户模块中内置方法 用来判断账号密码是与数据库匹配,如果匹配到返回用户对象
        #否则返回空
        user = authenticate(username=username, password=password)
        # 如果user不为空
        if user is not None:
            # 如果用户已经激活
            if user.is_active:
                # 记住登录状态
                login(request,user)
                # print(1)
                # 跳转到首页
                response =redirect(reverse('goods:index'))
                # 如果用户勾选了记住账户,设置cookie值,否则删除cookie的值
                if request.POST.get('remember')=='on':
                    response.set_cookie('username',username,max_age=7*24*3600)
                else:

                    response.delete_cookie('username')

                return response

            else:
                # 如果未激活返回错误信息
                return render(request, 'users/login.html', {'res': '账户未激活'})
        else:
            # 如果用户名密码验证失败返回错误信息
            return render(request, 'users/login.html',{'res':'用户名密码不正确'})


class Logout(View):
    """退出登录"""
    def get(self,request):
        # djang用户内置方法,退出登录
        logout(request)

        return redirect(reverse('goods:index'))