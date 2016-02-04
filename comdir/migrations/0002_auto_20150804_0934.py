# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comdir', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='branch_cities',
            field=models.ManyToManyField(related_name='branch_cities', null=True, to='comdir.City', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='n_of_employees',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
