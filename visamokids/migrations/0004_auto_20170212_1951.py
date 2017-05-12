# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visamokids', '0003_donor'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text=b'e.g. Sumanbhai', max_length=100, null=True, blank=True)),
                ('middle_name', models.CharField(help_text=b'e.g. Nenadiya', max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(help_text=b'e.g. Gamit', max_length=100, null=True, blank=True)),
                ('education_of_father', models.TextField(help_text=b'e.g. Studied till 10th grade', null=True, blank=True)),
                ('occupation_of_father', models.TextField(help_text=b'e.g. Business', null=True, blank=True)),
                ('contact_number', models.BigIntegerField(help_text=b'e.g. 8844999000', null=True, blank=True)),
                ('address', models.TextField(help_text=b'e.g. 8 Gomatipur Street, Sarkhej', null=True, blank=True)),
                ('district', models.TextField(help_text=b'e.g. Ahmedabad', null=True, blank=True)),
                ('monthly_income', models.BigIntegerField(help_text=b'e.g. 1333', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentMother',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text=b'e.g. Anitaben', max_length=100, null=True, blank=True)),
                ('education_of_mother', models.TextField(help_text=b'e.g. Studied till 10th grade', null=True, blank=True)),
                ('occupation_of_mother', models.TextField(help_text=b'e.g. Business', null=True, blank=True)),
                ('contact_number', models.BigIntegerField(help_text=b'e.g. 8844999000', null=True, blank=True)),
                ('monthly_income', models.BigIntegerField(help_text=b'e.g. 1333', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSchoolInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admission_secured_school', models.TextField(help_text=b'e.g. Anand Niketan School', null=True, blank=True)),
                ('date_of_admission_in_school', models.DateField(null=True, blank=True)),
                ('school_enrollment_number', models.BigIntegerField(help_text=b'e.g. 41', null=True, blank=True)),
                ('grade', models.CharField(help_text=b'e.g. 1st', max_length=5, null=True, blank=True)),
                ('aadhar_card_no', models.BigIntegerField(help_text=b'e.g. 957877658493', null=True, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='dt_of_joining',
            new_name='date_of_admission',
        ),
        migrations.RemoveField(
            model_name='student',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastname',
        ),
        migrations.AddField(
            model_name='student',
            name='birth_place',
            field=models.TextField(help_text=b'e.g. Uchhal ,Surat', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='caste',
            field=models.TextField(help_text=b'e.g. Hindu Gamit', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='findings',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(help_text=b'e.g. Arpit', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gr_no',
            field=models.BigIntegerField(help_text=b'e.g. 39', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='iq_result',
            field=models.IntegerField(help_text=b'e.g. 98', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='iq_test',
            field=models.CharField(default=b'No', max_length=3, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(help_text=b'e.g. Gamit', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='medical_report',
            field=models.CharField(default=b'No', max_length=3, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(help_text=b'e.g. Sumanbhai', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.TextField(help_text=b'e.g. Indian', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sc_st_obc',
            field=models.CharField(default=b'OTHER', max_length=5, choices=[(b'SC', b'SC'), (b'ST', b'ST'), (b'OBC', b'OBC'), (b'OTHER', b'Other')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='blood_group',
            field=models.CharField(help_text=b'e.g. O+ve', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_of_student',
            field=models.ForeignKey(blank=True, to='visamokids.StudentFather', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_of_student',
            field=models.ForeignKey(blank=True, to='visamokids.StudentMother', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_school_info',
            field=models.ForeignKey(blank=True, to='visamokids.StudentSchoolInfo', null=True),
        ),
    ]
