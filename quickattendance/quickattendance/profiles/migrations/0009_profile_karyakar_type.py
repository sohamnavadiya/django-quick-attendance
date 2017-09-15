# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='karyakar_type',
            field=models.CharField(choices=[('karyakar', 'karyakar'), ('nirikshak', 'nirikshak'), ('balkaryakar', 'balkaryakar'), ('visitor', 'visitor')], default='karyakar', max_length=20),
        ),
    ]