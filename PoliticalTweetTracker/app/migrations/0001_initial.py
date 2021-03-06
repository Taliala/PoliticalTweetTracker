# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('twitterHandle', models.CharField(max_length=50)),
                ('tweetId', models.BigIntegerField()),
                ('text', models.CharField(max_length=360)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
