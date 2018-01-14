from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
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

