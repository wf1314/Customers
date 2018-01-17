# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_mes',
            name='addr_id',
            field=models.ForeignKey(verbose_name='收货地址', to='users.Address'),
        ),
        migrations.AddField(
            model_name='order_mes',
            name='user_id',
            field=models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL),
        ),
    ]
