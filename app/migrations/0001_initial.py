# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectionData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('relevancy', models.CharField(max_length=200)),
                ('sentiment', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DailyPrices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
            name='LabledCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('stock', models.CharField(max_length=40)),
                ('counter', models.BigIntegerField(max_length=21)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('twitter_id', models.CharField(max_length=40)),
                ('user_id', models.CharField(max_length=200)),
                ('user_followers_count', models.IntegerField()),
                ('user_profile_image_url', models.CharField(max_length=500)),
                ('tweeter_name', models.CharField(max_length=100)),
                ('tweeter_sname', models.CharField(max_length=40)),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=100)),
                ('pub_date', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=600)),
                ('media_url', models.CharField(max_length=5000)),
                ('stock', models.CharField(max_length=40)),
                ('relevancy', models.CharField(max_length=40)),
                ('relevancy_second', models.CharField(max_length=40)),
                ('relevancy_third', models.CharField(max_length=40)),
                ('sentiment', models.CharField(max_length=40)),
                ('sentiment_second', models.CharField(max_length=40)),
                ('sentiment_third', models.CharField(max_length=40)),
                ('labeled_user', models.CharField(max_length=40)),
                ('labeled_user_second', models.CharField(max_length=40)),
                ('labeled_user_third', models.CharField(max_length=40)),
                ('voted_relevancy', models.CharField(max_length=40)),
                ('voted_sentiment', models.CharField(max_length=40)),
                ('labeled', models.BooleanField(default=False)),
                ('manual_labeled', models.BooleanField(default=False)),
                ('similarId', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelevancyCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('stock', models.CharField(max_length=40)),
                ('relevancy', models.CharField(max_length=200)),
                ('counter', models.BigIntegerField(max_length=21)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SentimentCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('stock', models.CharField(max_length=40)),
                ('sentiment', models.CharField(max_length=200)),
                ('counter', models.BigIntegerField(max_length=21)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('stock', models.CharField(max_length=40)),
                ('counter', models.BigIntegerField(max_length=21)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StocksPrices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('stock', models.CharField(max_length=40)),
                ('close', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('max', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('min', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('open', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('volume', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000.0)])),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
    ]
