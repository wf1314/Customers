# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_mes',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('order_id', models.CharField(serialize=False, verbose_name='订单id', max_length=128, primary_key=True)),
                ('pay_way', models.SmallIntegerField(choices=[(1, '支付宝'), (2, '微信'), (3, '银联'), (4, '货到付款')], verbose_name='支付方式', max_length=4)),
                ('total_count', models.IntegerField(default=1, verbose_name='商品数量')),
                ('total_price', models.DecimalField(default=1, decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('transport_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费')),
                ('pay_state', models.SmallIntegerField(default=1, choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')], verbose_name='订单状态', max_length=5)),
                ('pay_no', models.CharField(default='', verbose_name='支付编号', max_length=128)),
            ],
            options={
                'verbose_name_plural': '订单信息',
                'db_table': 'Order_mes',
                'verbose_name': '订单信息',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_count', models.IntegerField(default=1, verbose_name='商品数量')),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品历史价格')),
                ('goods_comment', models.CharField(verbose_name='商品评论', max_length=250)),
                ('goods_sku_id', models.ForeignKey(to='goods.GoodsSku', verbose_name='所属商品的sku')),
                ('order_mes_id', models.ForeignKey(to='orders.Order_mes', verbose_name='所属订单号')),
            ],
            options={
                'verbose_name_plural': '订单商品',
                'db_table': 'ordergoods',
                'verbose_name': '订单商品',
            },
        ),
    ]
