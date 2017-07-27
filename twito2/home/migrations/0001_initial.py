# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 14:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accesstoken', models.CharField(max_length=200)),
                ('accesskey', models.CharField(max_length=200)),
                ('accesstime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Application Access Info',
            },
        ),
        migrations.CreateModel(
            name='ApplicationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=200)),
                ('consumerkey', models.CharField(max_length=200)),
                ('consumertoken', models.CharField(max_length=200)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Application Info',
            },
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('appname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationData')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Activity',
            },
        ),
        migrations.AddField(
            model_name='applicationaccess',
            name='appname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicationData'),
        ),
        migrations.AddField(
            model_name='applicationaccess',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]