# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comdir', '0004_auto_20150804_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
