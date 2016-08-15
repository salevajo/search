# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 09:57
from __future__ import unicode_literals

from django.db import migrations, connection


def swap(name):
    ex = connection.cursor().execute
    ex('ALTER TABLE collector_{0} RENAME TO collector_tmp_{0}'.format(name))
    ex('ALTER TABLE search_{0} RENAME TO collector_{0}'.format(name))
    ex('ALTER TABLE collector_tmp_{0} RENAME TO search_{0}'.format(name))


def swap_tables(apps, schema_editor):
    oldCollection = apps.get_model('collector', 'Collection')
    for col in oldCollection.objects.all():
        print('old', col.loader)
        col.loader = col.loader.replace(
            'collector.loaders.',
            'hoover.search.loaders.',
        )
        col.save()

    newCollection = apps.get_model('search', 'Collection')
    for col in newCollection.objects.all():
        print('new', col.loader)
        col.loader = col.loader.replace(
            'hoover.search.loaders.',
            'collector.loaders.',
        )
        col.save()

    swap('collection')
    swap('collection_users')


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0011_auto_20160814_2040'),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(swap_tables, swap_tables),
    ]