# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-10 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0003_auto_20190110_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='blogPost.User'),
        ),
    ]
