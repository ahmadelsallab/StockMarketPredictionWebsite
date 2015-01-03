# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectionData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('relevancy', models.IntegerField(max_length=10, default=0, choices=[(1, 'Relevant'), (2, 'Irrelevant'), (0, 'Neutral')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Twitte',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('twitter_id', models.CharField(max_length=200)),
                ('user_id', models.CharField(unique=True, max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=200)),
                ('user_followers_count', models.IntegerField()),
                ('user_profile_image_url', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
