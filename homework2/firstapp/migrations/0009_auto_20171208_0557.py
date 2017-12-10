# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_auto_20171208_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=10, default='new', choices=[('editor', 'editor'), ('new', 'new')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(max_length=10, choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')]),
        ),
    ]
