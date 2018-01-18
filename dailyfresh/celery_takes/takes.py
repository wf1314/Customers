from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
django.setup()
from apps.goods.models import *



# 创建celery对象,设置中间队列为redis
app = Celery('dailyfresh', broker='redis://127.0.0.1:6379/5')


@app.task
def send_email(email,username,encrypt_user_id):

    subject = '天天生鲜'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [email]
    html_msg = """
        <h1>%s,欢迎您成为天天生鲜注册会员</h1>
        请点击以下链接激活您的账户<br/>
    <a href="http://127.0.0.1:8000/users/active/%s">http://127.0.0.1:8000/users/active/%s</a>
    """ %(username,encrypt_user_id,encrypt_user_id)

    send_mail(subject, message, sender, receiver,html_message=html_msg)

@app.task
def create_static_html():
    # 获取商品分类表的查询集对象
    goods_type = GoodsType.objects.all()
    # 获取首页图片轮播表查询集对象并按index排序
    good_activity = GoodsImgActivity.objects.all().order_by('Activity_img_index')
    # 获取促销活动表查询集对象
    sales = SalesPromotion.objects.all().order_by('promotion_index')
    # 获取商品分类对象
    for good in goods_type:
        # 通过商品分类对象向商品分类表中增加两个新的属性
        wenzi = GoodsTypeShow.objects.filter(goods_type_id=good, show_type=0).order_by('show_index')
        photo = GoodsTypeShow.objects.filter(goods_type_id=good, show_type=1).order_by('show_index')

        good.wenzi = wenzi
        good.photo = photo
    # 未登录用户购物车默认显示为0
    cart_count = 0

    static_temp = loader.get_template('goods/static_index.html')
    content = {'goods_type': goods_type,
               'good_activity': good_activity,
               'sales': sales,
               'cart_count': cart_count}

    res_html = static_temp.render(content)

    static_path = os.path.join(settings.BASE_DIR,'static/index.html')

    with open(static_path,'w') as f:
        f.write(res_html)

    print('生成静态页面成功')
