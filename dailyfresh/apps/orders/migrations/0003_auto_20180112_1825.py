# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180112_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_mes',
            name='pay_way',
            field=models.SmallIntegerField(choices=[(1, '支付宝'), (2, '微信'), (3, '银联'), (4, '货到付款')], verbose_name='支付方式'),
        ),
    ]
