''' models file '''
# pylint: disable=C0411,C0103,C0412,W0404
# type: ignore

from users.models import user
from django.db import models

# Create your models here.
from users.models import user
from room.models import room

class blog(models.Model):
    ''' blog class '''
    creator = models.ForeignKey(user,null=True,on_delete=models.SET_NULL)
    question = models.TextField(null=True,max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    room = models.ForeignKey(room,null=True,on_delete=models.SET_NULL)

class answer(models.Model):
    ''' answer class '''
    creator = models.ForeignKey(user,null=True,on_delete=models.SET_NULL)
    question =  models.ForeignKey(blog,null=True,on_delete=models.SET_NULL)
    answer = models.TextField(null=True,max_length=250)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    