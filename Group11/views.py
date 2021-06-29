# type: ignore
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import user

from room.models import room

@login_required(login_url='loginpage')
def home_page(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    obj = user.objects.filter(username=request.user).first()
    if obj.is_teacher:  
        rooms = room.objects.filter(creator=obj)
    else:
        rooms = room.objects.filter(students__username=request.user.username)
    size = rooms.__len__()
    content = {'obj':obj , 'rooms':rooms , 'size':size}
    return render(request, "home_page.html", content)

