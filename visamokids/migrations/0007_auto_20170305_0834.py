# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0006_auto_20170226_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='caste',
            field=models.CharField(default=b'None', max_length=300, null=True, help_text=b'e.g. Hindu Gamit', blank=True),
        ),
    ]
