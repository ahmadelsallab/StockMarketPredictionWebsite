# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150602_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPrices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('stock', models.CharField(max_length=40)),
                ('day', models.CharField(max_length=20)),
                ('min', models.CharField(max_length=20)),
                ('max', models.CharField(max_length=20)),
                ('concat', models.CharField(max_length=800)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('stock', models.CharField(max_length=40)),
                ('labeled_user', models.CharField(max_length=40)),
                ('relevancy', models.CharField(max_length=200)),
                ('counter', models.BigIntegerField(max_length=21)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeeklyPrices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('stock', models.CharField(max_length=40)),
                ('week', models.CharField(max_length=20)),
                ('min', models.CharField(max_length=20)),
                ('max', models.CharField(max_length=20)),
                ('concat', models.CharField(max_length=3500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='stocksprices',
            old_name='stock_price',
            new_name='close',
        ),
        migrations.AddField(
            model_name='stocksprices',
            name='max',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocksprices',
            name='min',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocksprices',
            name='open',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocksprices',
            name='volume',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000.0)]),
            preserve_default=False,
        ),
    ]
