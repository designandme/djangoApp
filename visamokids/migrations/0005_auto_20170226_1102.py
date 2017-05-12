# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0004_auto_20170212_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='donor',
            name='address',
            field=models.TextField(help_text=b'e.g. 8 Gomatipur Street, Sarkhej', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='annual_report',
            field=models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='child_pictures_available',
            field=models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='child_sponsored',
            field=models.ManyToManyField(to='visamokids.Student'),
        ),
        migrations.AddField(
            model_name='donor',
            name='child_story_available',
            field=models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='citizenship',
            field=models.CharField(help_text=b'e.g. Indian, US Citizen', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='contact_number',
            field=models.BigIntegerField(help_text=b'e.g. 8844999000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='dob',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='dob_family_member',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='email',
            field=models.EmailField(help_text=b'e.g. pradeep@factory.com', max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='first_name',
            field=models.CharField(help_text=b'e.g. Pradeep', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='is_35_ac_given',
            field=models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='is_80_G',
            field=models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='last_name',
            field=models.CharField(help_text=b'e.g. Khandwala', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='marriage_anniversary',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='progress_report',
            field=models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='reference',
            field=models.CharField(help_text=b'e.g. Pradeep', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='reminder_comments',
            field=models.TextField(help_text=b'Reminder sent to Pradeep', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='reminder_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='reminder_sent_flag',
            field=models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='sponsorship_amount',
            field=models.BigIntegerField(help_text=b'e.g. 3,60,000', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='sponsorship_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='sponsorship_nature',
            field=models.CharField(default=b'REG', max_length=3, null=True, blank=True, choices=[(b'REG', b'Regular Donor'), (b'NEW', b'New Donor')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='sponsorship_type',
            field=models.CharField(default=b'IND', max_length=3, null=True, blank=True, choices=[(b'IND', b'Individual'), (b'GRP', b'Group'), (b'INS', b'Institutional'), (b'CSR', b'CSR')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='gr_no',
            field=models.BigIntegerField(default=0, help_text=b'e.g. 39', serialize=False, primary_key=True),
        ),
    ]
