# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-23 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_image',
            field=models.CharField(max_length=500),
        ),
    ]
