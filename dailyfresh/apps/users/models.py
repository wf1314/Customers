from django.db import models
from db.base_model import BaseModel
# 导入django内置用户模块
from django.contrib.auth.models import AbstractUser




class AddressManager(models.Manager):
    """自定义管理器,用于返回默认的地址数据"""
    def show_def_addr(self,user):

        try:
            # 查询指定用户表中设置了默认的数据对象
            addr = self.model.objects.get(User_id=user,is_default=True)
        except self.model.DoesNotExist:
            addr = None

        return addr


# Create your models here.
class User(BaseModel,AbstractUser):

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(BaseModel):

    receiver = models.CharField(max_length=30, verbose_name='收件人')
    addr = models.CharField(max_length=200, verbose_name='地址')
    zip_code = models.CharField(max_length=6,null=True,blank=True,verbose_name='邮编')
    phone = models.CharField(max_length=11,verbose_name='联系方式')
    is_default = models.BooleanField(verbose_name='是否默认')
    User_id = models.ForeignKey('User',verbose_name='所属用户')

    objects = AddressManager()
    class Meta:
        db_table = 'address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
