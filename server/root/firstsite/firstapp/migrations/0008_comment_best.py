# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_comment_belong_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='best',
            field=models.BooleanField(default=False),
        ),
    ]
