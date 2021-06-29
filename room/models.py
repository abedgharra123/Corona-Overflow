# type: ignore
from django.db import models
from django import forms
from users.models import user

# Create your models here.


class room(models.Model):
    CHOICES = (
        ('SE', 'Software Engineering'),
        ('EE', 'Electrical Engineering'),
        ('CE', 'Chemical Engineering'),
        ('Ce', 'Civil Engineering'),
        ('ME', 'Mechanical Engineering'),
    )
    creator = models.CharField(max_length=100,null=False,default='abedgh')
    name = models.CharField(max_length=100,null=False,primary_key=True)
    students = models.ManyToManyField(user)
    subject = models.CharField(max_length=300, choices = CHOICES,default=CHOICES[0][0],null=True)


