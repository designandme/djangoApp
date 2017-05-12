# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0009_auto_20170408_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sponsorship_amount', models.BigIntegerField(help_text=b'e.g. 3,60,000', null=True, blank=True)),
                ('sponsorship_date', models.DateField(null=True, blank=True)),
                ('payment_details', models.TextField(help_text=b'e.g. Payment done with Paytm App. Amount credited to Paytm Number 9999888800. Amount credited is Rs 2,00,000.', null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='donor',
            name='sponsorship_amount',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='sponsorship_date',
        ),
        migrations.AddField(
            model_name='donor',
            name='in_kind_donation',
            field=models.TextField(help_text=b'e.g. In Kind Donation', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='sponsorship_sub_type',
            field=models.CharField(default=b'CMPLT', max_length=5, null=True, blank=True, choices=[(b'CMPLT', b'Complete Sponsorship'), (b'ANNUL', b'Annual Sponsorship For Education'), (b'SBFC', b'Sponsor Boarding, Food, Clothes'), (b'SM', b"Sponsor a Child's Meals"), (b'SB', b"Sponsor a Child's Boarding"), (b'SDM', b"Sponsor a Days's Meal"), (b'TD', b'Token Donation'), (b'IK', b'In Kind')]),
        ),
        migrations.AlterField(
            model_name='studentschoolinfo',
            name='grade',
            field=models.CharField(default=b'1', max_length=3, null=True, blank=True, choices=[(b'1', b'1st Grade'), (b'2', b'2nd Grade'), (b'3', b'3rd Grade'), (b'4', b'4th Grade'), (b'5', b'5th Grade'), (b'6', b'6th Grade'), (b'7', b'7th Grade'), (b'8', b'8th Grade'), (b'9', b'9th Grade'), (b'10', b'10th Grade'), (b'11', b'11th Science'), (b'11', b'11th Commerce'), (b'12', b'12th Science'), (b'12', b'12th Commerce')]),
        ),
        migrations.AddField(
            model_name='donor',
            name='payment_info',
            field=models.ForeignKey(blank=True, to='visamokids.PaymentInfo', null=True),
        ),
    ]
