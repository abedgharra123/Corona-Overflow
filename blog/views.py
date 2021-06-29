''' views moudle '''
# pylint: disable=C0411,C0301,E1101,C0103,E0402
# type: ignore
from django import http
from django.shortcuts import redirect, render

# Create your views here.

from .models import blog
from .models import answer

from room.models import room
from users.models import user
from Group11.forms import BlogModelForm,AnswerModelForm


def inside_room(request,name):
    ''' room function '''
    form = BlogModelForm(request.POST or None)
    form1 = AnswerModelForm(request.POST or None)

    obj = user.objects.filter(username=request.user).first()
    r = room.objects.get(name=name)
    blogs = blog.objects.filter(room=r).order_by('date').reverse()
    answers = answer.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            u = user.objects.get(username=request.user.username)
            obj.creator = u
            obj.room = room.objects.get(name=name)
            obj.save()
            form = BlogModelForm(None)
            return http.HttpResponseRedirect('.')

    content = {'blogs':blogs, 'obj':obj, 'name':name , 'answers':answers, 'form':form, 'form1':form1}
    return render(request,'inside_room.html',content)



def update_blog(request,name,pk):
    ''' function to update blog '''
    r = blog.objects.get(pk=pk)
    form = BlogModelForm(instance=r)
    if request.method == 'POST':
        form = BlogModelForm(request.POST,instance=r)
        if form.is_valid():
            obj = form.save(commit=False)
            u = user.objects.get(username=request.user.username)
            obj.creator = u
            obj.save()
            return redirect('inside-room',name)
    context = {'form':form ,'edit1':'edit1' , 'name':name }
    return render(request, 'update_blog.html',context)


def delete_blog(request,name,pk):
    ''' function to delete blog '''
    r = blog.objects.get(pk=pk)
    if request.method == 'POST':
        r.delete()
        for a in answer.objects.filter(question=r):
            a.delete()
        return redirect('inside-room',name)
    context = {'edit1':'edit1' , 'name':r.question }
    return render(request, 'delete_room.html',context)

def create_answer(request,pk,name):
    ''' function to create answer '''
    form1 = AnswerModelForm(request.POST or None)
    if request.method == 'POST':
        if form1.is_valid():
            obj = form1.save(commit=False)
            u = user.objects.get(username=request.user.username)
            obj.creator = u
            obj.question = blog.objects.get(pk=pk)
            obj.save()
    return redirect('inside-room',name)

def like_blog(request,pk,name):
    ''' function to like blog '''
    b = blog.objects.get(pk=pk)
    if b.likes%2==0:
        b.likes = b.likes + 1
    else:
        b.likes = b.likes - 1
    b.save()

    form = BlogModelForm(request.POST or None)
    form1 = AnswerModelForm(request.POST or None)

    obj = user.objects.filter(username=request.user).first()
    r = room.objects.get(name=name)
    blogs = blog.objects.filter(room=r).order_by('date').reverse()
    answers = answer.objects.all()

    content = {'blogs':blogs, 'obj':obj, 'name':name , 'answers':answers, 'form':form, 'form1':form1}
    return render(request,'inside_room.html',content)


def like_answer(request,pk,name):
    ''' function to like answer '''

    b = answer.objects.get(pk=pk)
    if b.likes%2==0:
        b.likes = b.likes + 1
    else:
        b.likes = b.likes - 1
    b.save()

    form = BlogModelForm(request.POST or None)
    form1 = AnswerModelForm(request.POST or None)

    obj = user.objects.filter(username=request.user).first()
    r = room.objects.get(name=name)
    blogs = blog.objects.filter(room=r).order_by('date').reverse()
    answers = answer.objects.all()

    content = {'blogs':blogs, 'obj':obj, 'name':name , 'answers':answers, 'form':form, 'form1':form1}
    return render(request,'inside_room.html',content)

def delete_answer(request,name,pk):
    ''' function to delete answer '''
    r = answer.objects.get(pk=pk)
    if request.method == 'POST':
        r.delete()
        return redirect('inside-room',name)
    context = {'edit1':'edit1' , 'name':r.answer }
    return render(request, 'delete_room.html',context)
