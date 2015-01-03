# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20141222_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('twitter_id', models.CharField(max_length=200)),
                ('user_id', models.CharField(unique=True, max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=200)),
                ('user_followers_count', models.IntegerField()),
                ('user_profile_image_url', models.CharField(max_length=500)),
                ('pub_date', models.CharField(max_length=200)),
                ('relevancy', models.CharField(max_length=200)),
                ('sentiment', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=100)),
                ('labeled', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=600)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
