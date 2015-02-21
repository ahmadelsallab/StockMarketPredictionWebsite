# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20141221_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('twitter_id', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=200, unique=True)),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=200)),
                ('user_followers_count', models.IntegerField()),
                ('user_profile_image_url', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('relevancy', models.CharField(max_length=200)),
                ('sentiment', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=100)),
                ('labeled', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Twitte',
        ),
    ]
