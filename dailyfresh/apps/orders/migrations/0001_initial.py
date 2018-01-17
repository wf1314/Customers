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
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('order_id', models.CharField(max_length=128, verbose_name='订单id', serialize=False, primary_key=True)),
                ('pay_way', models.SmallIntegerField(verbose_name='支付方式', choices=[(1, '支付宝'), (2, '微信'), (3, '银联'), (4, '货到付款')])),
                ('total_count', models.IntegerField(verbose_name='商品数量', default=1)),
                ('total_price', models.DecimalField(decimal_places=2, verbose_name='商品价格', default=1, max_digits=10)),
                ('transport_price', models.DecimalField(decimal_places=2, verbose_name='运费', max_digits=10)),
                ('pay_state', models.SmallIntegerField(verbose_name='订单状态', default=1, choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')])),
                ('pay_no', models.CharField(max_length=128, verbose_name='支付编号', default='')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'Order_mes',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('goods_count', models.IntegerField(verbose_name='商品数量', default=1)),
                ('goods_price', models.DecimalField(decimal_places=2, verbose_name='商品历史价格', max_digits=10)),
                ('goods_comment', models.CharField(max_length=250, verbose_name='商品评论')),
                ('goods_sku_id', models.ForeignKey(verbose_name='所属商品的sku', to='goods.GoodsSku')),
                ('order_mes_id', models.ForeignKey(verbose_name='所属订单号', to='orders.Order_mes')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
                'db_table': 'ordergoods',
            },
        ),
    ]
