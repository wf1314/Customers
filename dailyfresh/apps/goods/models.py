from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField

# Create your models here.


class GoodsType(BaseModel):
    """商品分类表"""
    type_name = models.CharField(max_length=20,verbose_name='分类名称')
    goods_logo = models.CharField(max_length=10,verbose_name='分类logo')
    type_img = models.ImageField(upload_to='goods/',verbose_name='分类图片')


    class Meta:

        db_table='goods_type'
        verbose_name='商品分类'
        verbose_name_plural=verbose_name

class GoodsSpu(BaseModel):
    """商品spu表"""
    goods_name = models.CharField(max_length=20,verbose_name='商品名称')
    goods_details = HTMLField(blank=True,verbose_name='商品详情')

    class Meta:
        db_table='goods_spu'
        verbose_name='商品spu'
        verbose_name_plural=verbose_name


class GoodsSku(BaseModel):
    """商品sku"""
    goods_state_tuple = (
        (1,'上架'),
        (2,'下架'),
    )

    goods_spu_id = models.ForeignKey('GoodsSpu',verbose_name='所属spu')
    goods_type_id = models.ForeignKey('GoodsType',verbose_name='所属分类')
    goods_name = models.CharField(max_length=20,verbose_name='商品SKU名称')
    goods_intro = models.CharField(max_length=256, verbose_name='商品简介')
    goods_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='商品价格')
    goods_unit = models.CharField(max_length=30,verbose_name='商品单位')
    goods_img = models.ImageField(upload_to='goods/',verbose_name='商品图片')

    goods_stock = models.IntegerField(default=0,verbose_name='商品库存')
    goods_annul = models.IntegerField(default=0,verbose_name='商品销量')
    goods_state = models.SmallIntegerField(choices=goods_state_tuple,default=2,verbose_name='商品状态')


    class Meta:
        db_table = 'goods_sku'
        verbose_name = '商品sku'
        verbose_name_plural = verbose_name


class GoodsImg(BaseModel):
    """商品图片"""

    goods_img = models.ImageField(upload_to='goods/',verbose_name='商品图片')
    goods_sku_id = models.ForeignKey('GoodsSku',verbose_name='所属商品sku')


    class Meta:
        db_table = 'goods_img'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class SalesPromotion(BaseModel):
    """首页促销活动表"""
    promotion_name = models.CharField(max_length=20,verbose_name='活动名称')
    promotion_addr = models.CharField(max_length=100,verbose_name='活动地址')

    promotion_img = models.ImageField(upload_to='goods',verbose_name='促销活动图片')
    promotion_index = models.SmallIntegerField(default=0,verbose_name='活动顺序')

    class Meta:
        db_table = 'sales_promotion'
        verbose_name = '商品促销活动'
        verbose_name_plural = verbose_name


class GoodsImgActivity(BaseModel):
    """首页图片轮播"""

    goods_sku_id = models.ForeignKey('GoodsSku',verbose_name='所属商品sku')

    Activity_img = models.ImageField(upload_to='goods',verbose_name='轮播图片')
    Activity_img_index = models.SmallIntegerField(default=0,verbose_name='轮播顺序')

    class Meta:
        db_table = 'goods_img_activity'
        verbose_name = '首页图片轮播'
        verbose_name_plural = verbose_name

class GoodsTypeShow(BaseModel):
    """商品分类展示"""

    show_type_tuple=(
        (0,'文字'),
        (1,'图片')
    )

    goods_type_id = models.ForeignKey('GoodsType', verbose_name='所属商品分类')
    goods_sku_id = models.ForeignKey('GoodsSku', verbose_name='所属商品sku')

    show_type = models.SmallIntegerField(choices=show_type_tuple,verbose_name='展示类型')
    show_index = models.SmallIntegerField(default=0,verbose_name='显示顺序')

    class Meta:
        db_table = 'goods_type_show'
        verbose_name = '首页商品分类展示'
        verbose_name_plural = verbose_name