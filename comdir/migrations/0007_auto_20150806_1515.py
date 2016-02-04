# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comdir', '0006_auto_20150806_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='services',
            field=models.ManyToManyField(to='comdir.Service'),
        ),
    ]
