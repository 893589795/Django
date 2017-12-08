# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20171206_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(max_length=10, choices=[('normal', 'normal'), ('dislike', 'dislike'), ('like', 'like')]),
        ),
    ]
