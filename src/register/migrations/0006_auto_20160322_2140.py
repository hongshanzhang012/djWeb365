# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlcontent',
            name='id',
        ),
        migrations.AlterField(
            model_name='urlcontent',
            name='url',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]
