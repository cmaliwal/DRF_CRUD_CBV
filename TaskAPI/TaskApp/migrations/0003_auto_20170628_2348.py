# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-28 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0002_task_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_created',
        ),
    ]
