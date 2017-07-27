# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 17:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170723_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationdata',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]