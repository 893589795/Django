# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0003_auto_20161105_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('avatar', models.ImageField(null=True, upload_to='upload')),
                ('sex', models.CharField(max_length=250, default='girl')),
                ('belong_to', models.ForeignKey(blank=True, null=True, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(max_length=10, choices=[('normal', 'normal'), ('dislike', 'dislike'), ('like', 'like')]),
        ),
    ]
