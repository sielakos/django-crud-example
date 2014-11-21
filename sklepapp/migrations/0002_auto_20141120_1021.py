# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklepapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(related_name='managed_departments', blank=True, to='sklepapp.Employee', null=True),
            preserve_default=True,
        ),
    ]
