# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comdir', '0005_auto_20150804_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='business_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
