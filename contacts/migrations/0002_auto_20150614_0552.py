# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=2)),
                ('postal_code', models.CharField(max_length=20)),
                ('contact', models.ForeignKey(to='contacts.Contact')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('contact', 'address_type')]),
        ),
    ]
