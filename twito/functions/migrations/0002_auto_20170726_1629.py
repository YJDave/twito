# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='twitterapp_user',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='twitterapp_user',
            name='app',
        ),
        migrations.RemoveField(
            model_name='twitterapp_user',
            name='user',
        ),
        migrations.AddField(
            model_name='twitterapp',
            name='access_key',
            field=models.TextField(default='Not Assigned', max_length=100),
        ),
        migrations.AddField(
            model_name='twitterapp',
            name='access_token',
            field=models.TextField(default='Not Assigned', max_length=100),
        ),
        migrations.DeleteModel(
            name='TwitterApp_User',
        ),
    ]