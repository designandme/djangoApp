# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0011_auto_20170506_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='payment_info',
        ),
        migrations.AddField(
            model_name='donor',
            name='payment_info',
            field=models.ManyToManyField(related_name='payment_info', to='visamokids.PaymentInfo'),
        ),
        migrations.RemoveField(
            model_name='donor',
            name='reminder_info',
        ),
        migrations.AddField(
            model_name='donor',
            name='reminder_info',
            field=models.ManyToManyField(related_name='reminder_info', to='visamokids.ReminderInfo'),
        ),
    ]
