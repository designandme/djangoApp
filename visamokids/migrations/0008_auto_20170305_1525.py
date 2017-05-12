# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0007_auto_20170305_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='child_sponsored',
            field=models.ManyToManyField(related_name='student', to='visamokids.Student'),
        ),
    ]
