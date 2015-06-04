# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='stocksprices',
            old_name='stock_name',
            new_name='stock',
        ),
        migrations.AddField(
            model_name='opinion',
            name='manual_labeled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
