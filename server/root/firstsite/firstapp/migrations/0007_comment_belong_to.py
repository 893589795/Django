# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='belong_to',
            field=models.ForeignKey(blank=True, null=True, related_name='article_comments', to='firstapp.Article'),
        ),
    ]
