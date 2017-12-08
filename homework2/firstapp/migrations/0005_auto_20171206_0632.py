# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20171206_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(max_length=10, choices=[('dislike', 'dislike'), ('like', 'like'), ('normal', 'normal')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(max_length=10, choices=[('woman', 'woman'), ('man', 'man')]),
        ),
    ]
