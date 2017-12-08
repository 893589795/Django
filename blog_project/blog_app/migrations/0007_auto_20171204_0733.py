# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20171204_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.FileField(null=True, upload_to='cover_image'),
        ),
    ]
