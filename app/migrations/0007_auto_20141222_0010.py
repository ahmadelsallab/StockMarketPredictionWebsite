# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20141221_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='pub_date',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
