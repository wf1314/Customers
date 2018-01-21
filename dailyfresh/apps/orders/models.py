from django.db import models
from db.base_model import BaseModel
# Create your models here.


class Order_mes(BaseModel):
    """订单信息表"""
    pay_way_tuple = (
        (1,'支付宝'),
        (2,'微信'),
        (3,'银联'),
        (4,'货到付款'),

    )
    pay_dict={
        '1':'支付宝',
        '2':'微信',
        '3':'银联',
        '4':'货到付款'
    }
    pay_state_tuple =(
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成')
    )

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单id')
    pay_way = models.SmallIntegerField(choices=pay_way_tuple,verbose_name='支付方式')
    total_count = models.IntegerField(default=1,verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=1,verbose_name='商品价格')
    transport_price= models.DecimalField(max_digits=10,decimal_places=2,verbose_name='运费')
    pay_state = models.SmallIntegerField(choices=pay_state_tuple,default=1,verbose_name='订单状态')
    pay_no = models.CharField(max_length=128, default='', verbose_name='支付编号')
    user_id = models.ForeignKey('users.User',verbose_name='所属用户')
    addr_id = models.ForeignKey('users.Address',verbose_name='收货地址')

    class Meta:

        db_table='Order_mes'
        verbose_name='订单信息'
        verbose_name_plural= verbose_name

class OrderGoods(BaseModel):
    """订单商品表"""
    goods_count = models.IntegerField(default=1,verbose_name='商品数量')
    goods_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='商品历史价格')
    goods_comment = models.CharField(max_length=250,verbose_name='商品评论')
    order_mes_id = models.ForeignKey('Order_mes',verbose_name='所属订单号')
    goods_sku_id = models.ForeignKey('goods.GoodsSku',verbose_name='所属商品的sku')

    class Meta:

        db_table='ordergoods'
        verbose_name='订单商品'
        verbose_name_plural= verbose_name