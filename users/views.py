# type: ignore
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import user


from Group11.forms import RegisterForm


def users_list(request):
    lst = user.objects.all()
    template_name = 'users_list.html'
    context = {'objects': lst}
    return render(request, template_name, context)

######################################

def Register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('loginpage')
    template_name = 'register.html'
    context = {'form':form}
    
    return render(request, template_name, context)
    
def loginpage(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    template_name = 'login.html'
    return render(request, template_name)

@login_required(login_url='loginpage')
def logoutpage(request):
    logout(request)
    return redirect('loginpage')