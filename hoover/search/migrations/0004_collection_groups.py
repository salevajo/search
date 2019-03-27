# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-15 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('search', '0003_update_snoop_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='hoover_search_collections', to='auth.Group'),
        ),
    ]
