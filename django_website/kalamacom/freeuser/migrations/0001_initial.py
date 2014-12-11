# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=1000)),
                ('sentiment', models.IntegerField(default=2, max_length=10, choices=[(0, 'Positive'), (1, 'Negative'), (2, 'Neutral')])),
                ('source_url', models.CharField(default='Unknown', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
