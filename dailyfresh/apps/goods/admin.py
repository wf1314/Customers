from django.contrib import admin
from .models import *
# Register your models here.
from django.core.cache import cache


class BaseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        from celery_takes.takes import create_static_html

        create_static_html.delay()
        cache.delete('index_data')
    def delete_model(self, request, obj):
        super().delete_model(request,obj)
        from celery_takes.takes import create_static_html

        create_static_html.delay()
        cache.delete('index_data')


class GoodsTypeAdmin(BaseAdmin):
    pass


class SalesPromotionAdmin(BaseAdmin):
    pass


class GoodsImgActivityAdmin(BaseAdmin):
    pass


class GoodsTypeShowAdmin(BaseAdmin):
    pass


admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(SalesPromotion,SalesPromotionAdmin)
admin.site.register(GoodsImgActivity,GoodsImgActivityAdmin)
admin.site.register(GoodsTypeShow,GoodsTypeShowAdmin)