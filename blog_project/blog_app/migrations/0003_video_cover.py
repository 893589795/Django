# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_remove_video_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='cover',
            field=models.FileField(null=True, upload_to='cover_image'),
        ),
    ]
