# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_urlcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlcontent',
            name='md5',
            field=models.CharField(default=10, max_length=32, blank=True),
        ),
    ]
