from django.db import models
from django import forms
from django.conf import settings

from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True

# Create your models here.



class user(User):
    CHOICES = (
        ('SE', 'Software Engineering'),
        ('EE', 'Electrical Engineering'),
        ('CE', 'Chemical Engineering'),
        ('Ce', 'Civil Engineering'),
        ('ME', 'Mechanical Engineering'),
    )
    CHOICES1 = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    is_teacher = models.BooleanField(default=False)
    year = models.CharField(max_length=300, choices = CHOICES1,default=CHOICES1[0][0])
    subject = models.CharField(max_length=300, choices = CHOICES,default=CHOICES[0][0])
    



