# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('url', models.URLField()),
                ('logo_url', models.URLField(null=True)),
                ('n_of_employees', models.IntegerField(null=True)),
                ('branch_cities', models.ManyToManyField(related_name='branch_cities', null=True, to='comdir.City')),
                ('city', models.ForeignKey(related_name='headquarters_city', to='comdir.City')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='tags',
            field=models.ManyToManyField(to='comdir.Tag'),
        ),
    ]
