from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from itsdangerous import TimedJSONWebSignatureSerializer,SignatureExpired
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from celery_takes.takes import send_email
import re


# Create your views here.
class Register(View):
    def get(self, request):

        return render(request, 'users/register.html')

    def post(self, request):

        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        # print(1)
        if not all([username, pwd, email]):
            print(2)
            return render(request, 'users/register.html', {'res': '注册信息有误'})

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            print(3)
            return render(request, 'users/register.html', {'res': '邮箱格式错误'})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user=None

        if user:
            return render(request, 'users/register.html', {'res': '用户名已存在'})
        #
        user = User.objects.create_user(username, email, pwd)
        user.is_active = 0
        user.save()



        #
        seria = TimedJSONWebSignatureSerializer(settings.SECRET_KEY,3600)

        dict1 = {
            'user_id':user.id
        }
        encrypt_user_id = seria.dumps(dict1)
        encrypt_user_id = encrypt_user_id.decode()

        send_email.delay(email,username,encrypt_user_id)

        #
        #
        # subject = '天天生鲜'
        # message = ''
        # sender = settings.EMAIL_FROM
        # receiver = [email]
        # html_msg = """
        #     <h1>%s,欢迎您成为天天生鲜注册会员</h1>
        #     请点击以下链接激活您的账户<br/>
        # <a href="http://127.0.0.1:8000/users/active/%s">http://127.0.0.1:8000/users/active/%s</a>
        # """ %(user.username,encrypt_user_id,encrypt_user_id)
        #
        # send_mail(subject, message, sender, receiver,html_message=html_msg)



        return redirect(reverse('goods:index'))


class Active(View):

    def get(self,request,token):
        seria = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 3600)

        try:
            print(token)
            user_id = seria.loads(token)
            print(user_id, user_id['user_id'])
            user = User.objects.get(id=user_id['user_id'])
            user.is_active=1
            return redirect(reverse('users:login'))
        except SignatureExpired as e:
            return HttpResponse('<h1>链接已过期</h1>')

class Login(View):

    def get(self,request):

        return render(request,'users/login.html')
