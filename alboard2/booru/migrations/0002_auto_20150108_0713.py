# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('booru', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pool',
            options={'ordering': ['-start_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='signature',
            field=models.CharField(db_index=True, max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
