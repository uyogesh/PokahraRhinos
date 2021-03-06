# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('citizenship_no', models.CharField(max_length=100)),
                ('place_of_issue', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('residential_add', models.TextField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('played_for', models.CharField(choices=[('Club Level', 'Club Level'), ('School Level', 'School Level'), ('Casual', 'Casual'), ('Locality', 'Locality')], max_length=20)),
                ('bowling_arm', models.CharField(choices=[('Left Arm', 'Left Arm'), ('Right Arm', 'Right Arm'), ('Both', 'Both')], max_length=20)),
                ('bowling_pace', models.CharField(choices=[('Med Pace', 'Med Pace'), ('Spinner', 'Spinner'), ('Fast', 'Fast')], max_length=20)),
                ('wicket_keeper', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('club_name', models.CharField(max_length=100)),
                ('batting', models.CharField(choices=[('Left Hand', 'Left Hand'), ('Right Hand', 'Right Hand')], max_length=20)),
                ('first_preference', models.CharField(choices=[('Batting', 'Batting'), ('Bowling', 'Bowling')], max_length=20)),
                ('team_captain_experience', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('health_issues', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('other_details', models.CharField(max_length=100)),
            ],
        ),
    ]
