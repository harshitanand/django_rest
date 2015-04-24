# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150415_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieslist',
            name='name',
            field=models.CharField(unique=True, max_length=150),
            preserve_default=True,
        ),
    ]
