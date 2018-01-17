# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsImg',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('goods_img', models.ImageField(verbose_name='商品图片', upload_to='goods/')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
                'db_table': 'goods_img',
            },
        ),
        migrations.CreateModel(
            name='GoodsImgActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('Activity_img', models.ImageField(verbose_name='轮播图片', upload_to='goods')),
                ('Activity_img_index', models.SmallIntegerField(verbose_name='轮播顺序', default=0)),
            ],
            options={
                'verbose_name': '首页图片轮播',
                'verbose_name_plural': '首页图片轮播',
                'db_table': 'goods_img_activity',
            },
        ),
        migrations.CreateModel(
            name='GoodsSku',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('goods_name', models.CharField(max_length=20, verbose_name='商品SKU名称')),
                ('goods_intro', models.CharField(max_length=256, verbose_name='商品简介')),
                ('goods_price', models.DecimalField(decimal_places=2, verbose_name='商品价格', max_digits=10)),
                ('goods_unit', models.CharField(max_length=30, verbose_name='商品单位')),
                ('goods_img', models.ImageField(verbose_name='商品图片', upload_to='goods/')),
                ('goods_stock', models.IntegerField(verbose_name='商品库存', default=0)),
                ('goods_annul', models.IntegerField(verbose_name='商品销量', default=0)),
                ('goods_state', models.SmallIntegerField(verbose_name='商品状态', default=2, choices=[(1, '上架'), (2, '下架')])),
            ],
            options={
                'verbose_name': '商品sku',
                'verbose_name_plural': '商品sku',
                'db_table': 'goods_sku',
            },
        ),
        migrations.CreateModel(
            name='GoodsSpu',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('goods_name', models.CharField(max_length=20, verbose_name='商品名称')),
                ('goods_details', tinymce.models.HTMLField(blank=True, verbose_name='商品详情')),
            ],
            options={
                'verbose_name': '商品spu',
                'verbose_name_plural': '商品spu',
                'db_table': 'goods_spu',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('type_name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('goods_logo', models.CharField(max_length=10, verbose_name='分类logo')),
                ('type_img', models.ImageField(verbose_name='分类图片', upload_to='goods/')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
                'db_table': 'goods_type',
            },
        ),
        migrations.CreateModel(
            name='GoodsTypeShow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('show_type', models.SmallIntegerField(verbose_name='展示类型', choices=[(1, '文字'), (2, '图片')])),
                ('show_index', models.SmallIntegerField(verbose_name='显示顺序', default=0)),
                ('goods_sku_id', models.ForeignKey(verbose_name='所属商品sku', to='goods.GoodsSku')),
                ('goods_type_id', models.ForeignKey(verbose_name='所属商品分类', to='goods.GoodsType')),
            ],
            options={
                'verbose_name': '首页商品分类展示',
                'verbose_name_plural': '首页商品分类展示',
                'db_table': 'goods_type_show',
            },
        ),
        migrations.CreateModel(
            name='SalesPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('promotion_name', models.CharField(max_length=20, verbose_name='活动名称')),
                ('promotion_addr', models.CharField(max_length=100, verbose_name='活动地址')),
                ('promotion_img', models.ImageField(verbose_name='促销活动图片', upload_to='goods')),
                ('promotion_index', models.SmallIntegerField(verbose_name='活动顺序', default=0)),
            ],
            options={
                'verbose_name': '商品促销活动',
                'verbose_name_plural': '商品促销活动',
                'db_table': 'sales_promotion',
            },
        ),
        migrations.AddField(
            model_name='goodssku',
            name='goods_spu_id',
            field=models.ForeignKey(verbose_name='所属spu', to='goods.GoodsSpu'),
        ),
        migrations.AddField(
            model_name='goodssku',
            name='goods_type_id',
            field=models.ForeignKey(verbose_name='所属分类', to='goods.GoodsType'),
        ),
        migrations.AddField(
            model_name='goodsimgactivity',
            name='goods_sku_id',
            field=models.ForeignKey(verbose_name='所属商品sku', to='goods.GoodsSku'),
        ),
        migrations.AddField(
            model_name='goodsimg',
            name='goods_sku_id',
            field=models.ForeignKey(verbose_name='所属商品sku', to='goods.GoodsSku'),
        ),
    ]
