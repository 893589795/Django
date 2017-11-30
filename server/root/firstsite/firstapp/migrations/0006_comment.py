# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20171123_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('avatar', models.CharField(max_length=100, default='static/images/default.png')),
                ('content', models.TextField()),
                ('createtime', models.DateField(auto_now=True)),
            ],
        ),
    ]
