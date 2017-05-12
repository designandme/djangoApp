# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0005_auto_20170226_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_place',
            field=models.CharField(help_text=b'e.g. Uchhal ,Surat', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='caste',
            field=models.CharField(help_text=b'e.g. Hindu Gamit', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='findings',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(help_text=b'e.g. Indian', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentfather',
            name='district',
            field=models.CharField(help_text=b'e.g. Ahmedabad', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentfather',
            name='education_of_father',
            field=models.CharField(help_text=b'e.g. Studied till 10th grade', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentfather',
            name='occupation_of_father',
            field=models.CharField(help_text=b'e.g. Business', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentmother',
            name='education_of_mother',
            field=models.CharField(help_text=b'e.g. Studied till 10th grade', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentmother',
            name='occupation_of_mother',
            field=models.CharField(help_text=b'e.g. Business', max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studentschoolinfo',
            name='admission_secured_school',
            field=models.CharField(help_text=b'e.g. Anand Niketan School', max_length=300, null=True, blank=True),
        ),
    ]
