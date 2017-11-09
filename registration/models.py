# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Model
# Create your models here.


class RegistrationFormModel(Model):
    first_name = models.CharField(max_length=50,null=False,verbose_name='*First Name')
    middle_name = models.CharField(max_length=50,verbose_name='Middle Name',default="None")
    last_name = models.CharField(max_length=50,null=False,verbose_name='*Last Name')
    dob = models.DateField(verbose_name='*Date of Birth',default='2017-10-10')
    citizenship_no = models.CharField(max_length=100,null=False,verbose_name='*Citizenship Number')
    place_of_issue = models.CharField(max_length=100,null=False,verbose_name='*Place Of Issue')
    mobile_no = models.CharField(max_length=10,null=False,verbose_name='*Mobile Number')
    residential_add = models.TextField(max_length=100,null=False,verbose_name='*Residential Address')
    email = models.CharField(max_length=100,null=False,verbose_name='*Email')
    sex = models.CharField(max_length=100,null=False,verbose_name='*Sex')
    height = models.CharField(null=False,verbose_name='*Height',max_length=20)
    weight = models.IntegerField(null=False,verbose_name='*Weight')
    played_for = models.CharField(max_length=20,choices=[('Club Level','Club Level'),('School Level','School Level'),
                                                         ('Casual','Casual'),('Locality','Locality')],default='Select')
    bowling_arm = models.CharField(max_length=20,choices=[('Left Arm','Left Arm'),('Right Arm','Right Arm'),('Both','Both')],default='Select')
    bowling_pace = models.CharField(max_length=20,choices=[('Med Pace','Med Pace'),('Spinner','Spinner'),('Fast','Fast')],default='Select')
    wicket_keeper = models.CharField(max_length=20,choices=[('Yes','Yes'),('No','No')],default='Select')
    club_name = models.CharField(max_length=100)
    batting = models.CharField(max_length=20,choices=[('Left Hand','Left Hand'),('Right Hand','Right Hand')],default='Select')
    first_preference = models.CharField(max_length=20,choices=[('Batting','Batting'),('Bowling','Bowling')],default='Select')
    team_captain_experience = models.CharField(max_length=20,choices=[('Yes','Yes'),('No','No')],default='Select')
    health_issues = models.CharField(max_length=20,choices=[('Yes','Yes'),('No','No')],default='Select')
    other_details = models.CharField(max_length=100)





