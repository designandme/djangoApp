# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0010_auto_20170506_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reminder_sent_flag', models.CharField(default=b'Y', max_length=3, null=True, blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('reminder_date', models.DateField(null=True, blank=True)),
                ('reminder_comments', models.TextField(help_text=b'Reminder sent to Pradeep', null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='donor',
            name='reminder_comments',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='reminder_date',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='reminder_sent_flag',
        ),
        migrations.AddField(
            model_name='donor',
            name='reminder_info',
            field=models.ForeignKey(blank=True, to='visamokids.ReminderInfo', null=True),
        ),
    ]
