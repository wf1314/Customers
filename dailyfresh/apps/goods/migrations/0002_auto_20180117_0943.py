# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodstypeshow',
            name='show_type',
            field=models.SmallIntegerField(choices=[(0, '文字'), (1, '图片')], verbose_name='展示类型'),
        ),
    ]
