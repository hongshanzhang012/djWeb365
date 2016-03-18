# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=128)),
                ('md5', models.BinaryField(default=10, max_length=32, blank=True)),
                ('modified', models.DateTimeField(blank=True)),
            ],
        ),
    ]
