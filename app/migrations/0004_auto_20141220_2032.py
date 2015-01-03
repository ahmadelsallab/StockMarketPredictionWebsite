# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141220_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='StocksPrices',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=200)),
                ('stock_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='correctiondata',
            name='sentiment',
            field=models.CharField(max_length=200, default='Positive'),
            preserve_default=False,
        ),
    ]
