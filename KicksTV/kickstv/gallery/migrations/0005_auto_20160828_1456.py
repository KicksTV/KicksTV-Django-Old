# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-28 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_gallery_gallery_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image',
            field=models.FileField(upload_to=b''),
        ),
    ]
