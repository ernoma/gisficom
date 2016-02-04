# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comdir', '0003_auto_20150804_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.TextField(max_length=200),
        ),
    ]
