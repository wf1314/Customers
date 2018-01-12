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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_img', models.ImageField(verbose_name='商品图片', upload_to='goods/')),
            ],
            options={
                'verbose_name_plural': '商品图片',
                'db_table': 'goods_img',
                'verbose_name': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='GoodsImgActivity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('Activity_img', models.ImageField(verbose_name='轮播图片', upload_to='goods')),
                ('Activity_img_index', models.SmallIntegerField(default=0, verbose_name='轮播顺序')),
            ],
            options={
                'verbose_name_plural': '首页图片轮播',
                'db_table': 'goods_img_activity',
                'verbose_name': '首页图片轮播',
            },
        ),
        migrations.CreateModel(
            name='GoodsSku',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_name', models.CharField(verbose_name='商品SKU名称', max_length=20)),
                ('goods_intro', models.CharField(verbose_name='商品简介', max_length=256)),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('goods_unit', models.CharField(verbose_name='商品单位', max_length=30)),
                ('goods_stock', models.IntegerField(default=0, verbose_name='商品库存')),
                ('goods_annul', models.IntegerField(default=0, verbose_name='商品销量')),
                ('goods_state', models.SmallIntegerField(default=2, choices=[(1, '上架'), (2, '下架')], verbose_name='商品状态')),
                ('goods_img', models.ImageField(verbose_name='商品图片', upload_to='goods/')),
            ],
            options={
                'verbose_name_plural': '商品sku',
                'db_table': 'goods_sku',
                'verbose_name': '商品sku',
            },
        ),
        migrations.CreateModel(
            name='GoodsSpu',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_name', models.CharField(verbose_name='商品名称', max_length=20)),
                ('goods_details', tinymce.models.HTMLField(blank=True, verbose_name='商品详情')),
            ],
            options={
                'verbose_name_plural': '商品spu',
                'db_table': 'goods_spu',
                'verbose_name': '商品spu',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('type_name', models.CharField(verbose_name='分类名称', max_length=20)),
                ('goods_logo', models.CharField(verbose_name='分类logo', max_length=10)),
                ('type_img', models.ImageField(verbose_name='分类图片', upload_to='goods/')),
            ],
            options={
                'verbose_name_plural': '商品分类',
                'db_table': 'goods_type',
                'verbose_name': '商品分类',
            },
        ),
        migrations.CreateModel(
            name='GoodsTypeShow',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('show_type', models.SmallIntegerField(choices=[(1, '文字'), (2, '图片')], verbose_name='展示类型')),
                ('show_index', models.SmallIntegerField(default=0, verbose_name='显示顺序')),
                ('goods_sku_id', models.ForeignKey(to='goods.GoodsSku', verbose_name='所属商品sku')),
                ('goods_type_id', models.ForeignKey(to='goods.GoodsType', verbose_name='所属商品分类')),
            ],
            options={
                'verbose_name_plural': '首页商品分类展示',
                'db_table': 'goods_type_show',
                'verbose_name': '首页商品分类展示',
            },
        ),
        migrations.CreateModel(
            name='SalesPromotion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('promotion_name', models.CharField(verbose_name='活动名称', max_length=20)),
                ('promotion_img', models.ImageField(verbose_name='促销活动图片', upload_to='goods')),
                ('promotion_addr', models.CharField(verbose_name='活动地址', max_length=100)),
                ('promotion_index', models.SmallIntegerField(default=0, verbose_name='活动顺序')),
            ],
            options={
                'verbose_name_plural': '商品促销活动',
                'db_table': 'sales_promotion',
                'verbose_name': '商品促销活动',
            },
        ),
        migrations.AddField(
            model_name='goodssku',
            name='goods_spu_id',
            field=models.ForeignKey(to='goods.GoodsSpu', verbose_name='所属spu'),
        ),
        migrations.AddField(
            model_name='goodssku',
            name='goods_type_id',
            field=models.ForeignKey(to='goods.GoodsType', verbose_name='所属分类'),
        ),
        migrations.AddField(
            model_name='goodsimgactivity',
            name='goods_sku_id',
            field=models.ForeignKey(to='goods.GoodsSku', verbose_name='所属商品sku'),
        ),
        migrations.AddField(
            model_name='goodsimg',
            name='goods_sku_id',
            field=models.ForeignKey(to='goods.GoodsSku', verbose_name='所属商品sku'),
        ),
    ]
