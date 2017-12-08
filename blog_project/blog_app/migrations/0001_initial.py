# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('url_image', models.URLField(blank=True, null=True)),
                ('cover', models.FileField(null=True, upload_to='cover_image')),
                ('editors_choice', models.BooleanField(default=False)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('readers', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
