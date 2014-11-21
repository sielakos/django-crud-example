# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklepapp', '0002_auto_20141120_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, to='sklepapp.Department', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ForeignKey(blank=True, to='sklepapp.Department', null=True),
            preserve_default=True,
        ),
    ]
