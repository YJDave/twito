# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 16:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationaccess',
            old_name='accesskey',
            new_name='accesssecret',
        ),
        migrations.RenameField(
            model_name='applicationdata',
            old_name='consumertoken',
            new_name='consumersecret',
        ),
    ]
