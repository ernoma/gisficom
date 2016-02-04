# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comdir', '0002_auto_20150804_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AddField(
            model_name='company',
            name='business_id',
            field=models.CharField(max_length=200, unique=True, null=True, blank=True),
        ),
    ]
