# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-11 09:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogPost', '0005_auto_20190110_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='user',
        ),
        migrations.AddField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
