# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170218_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='sample-title'),
            preserve_default=False,
        ),
    ]