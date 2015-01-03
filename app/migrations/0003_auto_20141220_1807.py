# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141210_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='correctiondata',
            name='stock',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='correctiondata',
            name='relevancy',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
