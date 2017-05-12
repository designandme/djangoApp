# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0008_auto_20170305_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='sponsorship_sub_type',
            field=models.CharField(default=b'CMPLT', max_length=5, null=True, blank=True, choices=[(b'CMPLT', b'Complete Sponsorship'), (b'ANNUL', b'Annual Sponsorship For Education'), (b'SBFC', b'Sponsor Boarding, Food, Clothes'), (b'SM', b"Sponsor a Child's Meals"), (b'SB', b"Sponsor a Child's Boarding"), (b'SDM', b"Sponsor a Days's Meal"), (b'TD', b'Token Donation')]),
        ),
        migrations.AddField(
            model_name='student',
            name='bio',
            field=models.TextField(help_text=b'e.g. Has four siblings. Two younger and two elder ones.. or.. Started working as developer in TCS.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='studentschoolinfo',
            name='status',
            field=models.CharField(default=b'STU', max_length=3, null=True, blank=True, choices=[(b'STU', b'Studying'), (b'DRP', b'Drop Out'), (b'PSD', b'Passed Out')]),
        ),
        migrations.AlterField(
            model_name='studentschoolinfo',
            name='grade',
            field=models.CharField(default=b'1', max_length=3, null=True, blank=True, choices=[(b'1', b'1st Grade'), (b'2', b'2nd Grade'), (b'3', b'3rd Grade'), (b'4', b'4th Grade'), (b'5', b'5th Grade'), (b'6', b'6th Grade'), (b'7', b'7th Grade'), (b'8', b'8th Grade'), (b'9', b'9th Grade'), (b'10', b'10th Grade'), (b'11', b'11th Grade'), (b'12', b'12th Grade')]),
        ),
    ]
