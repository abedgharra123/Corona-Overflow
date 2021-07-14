# type: ignore
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required 


from Group11.forms import RoomModelForm
# Create your views here.
from users.models import user
from room.models import room

@login_required(login_url='loginpage')
def create_room(request):
    u = user.objects.get(username=request.user.username)
    if not u.is_teacher:
        return HttpResponse('Page not found', status=404)
    form = RoomModelForm(u)
    if request.method == 'POST':
        form = RoomModelForm(u, request.POST )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user.username
            obj.subject = u.subject 
            obj.save()
            form.save_m2m()
            return redirect('home')
    template_name = 'create_room.html'
    context = {'form':form } 
    return render(request, template_name, context)


@login_required(login_url='loginpage')
def update_room(request,name):
    u = user.objects.get(username=request.user.username)
    r = room.objects.get(name=name)
    form = RoomModelForm(u,instance=r)
    if request.method == 'POST':
        form = RoomModelForm(u,request.POST,instance=r)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user.username
            obj.save()
            form.save_m2m()
            return redirect('home')
    context = {'form':form ,'edit':'edit' , 'name':name } 
    return render(request, 'create_room.html',context)


@login_required(login_url='loginpage')
def delete_room(request,name):
    r = room.objects.get(name=name)
    if request.method == 'POST':
        r.delete()
        return redirect('home')
    context = {'edit':'edit' , 'name':name } 
    return render(request, 'delete_room.html',context)