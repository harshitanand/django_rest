# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('popularity', models.FloatField(default=b'0.0', blank=True)),
                ('director', models.TextField(default=b' ', max_length=100, blank=True)),
                ('genre', models.CharField(default=b'Drama', max_length=100, choices=[(b'Adventure', b'Adventure'), (b'Crime', b'Crime'), (b'Drama', b'Drama'), (b'Family', b'Family'), (b'Fantasy', b'Fantasy'), (b'Horror', b'Horror'), (b'Musical', b'Musical'), (b'Mystery', b'Mystery'), (b'Romance', b'Romance'), (b'Sci-Fi', b'Sci-Fi'), (b'Thriller', b'Thriller'), (b'War', b'War'), (b'Western', b'Western')])),
                ('imdb_score', models.FloatField(default=b'0.5')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
