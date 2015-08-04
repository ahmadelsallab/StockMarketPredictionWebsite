# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='conversation_reply',
            field=models.CharField(default=10000000, max_length=40),
            preserve_default=False,
        ),
    ]
