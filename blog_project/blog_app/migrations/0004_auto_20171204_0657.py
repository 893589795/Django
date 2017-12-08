# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_video_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover_image'),
        ),
    ]
