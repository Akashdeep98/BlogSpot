# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-10 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0002_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='author',
            field=models.CharField(max_length=264, null=True),
        ),
    ]