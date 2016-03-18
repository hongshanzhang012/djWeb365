# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('content_change', models.BooleanField(default=False)),
                ('server_is_down', models.BooleanField(default=False)),
            ],
        ),
    ]
