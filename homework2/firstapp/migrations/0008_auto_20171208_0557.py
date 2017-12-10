# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20171207_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=10, default='new', choices=[('new', 'new'), ('editor', 'editor')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(max_length=10, choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')]),
        ),
    ]
