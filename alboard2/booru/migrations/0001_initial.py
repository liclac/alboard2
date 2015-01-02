# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='', width_field='width', height_field='height')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('signature', models.CharField(blank=True, max_length=30)),
                ('pool', models.ForeignKey(to='booru.Pool')),
            ],
            options={
                'ordering': ['created_at'],
            },
            bases=(models.Model,),
        ),
    ]
