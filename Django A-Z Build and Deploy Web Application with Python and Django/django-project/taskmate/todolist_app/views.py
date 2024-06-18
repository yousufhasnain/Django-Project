from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator # use for create pagination
from django.contrib.auth.decorators import login_required

""" for restriction of different page django uses login_required decorators default function 
steps:
1. @login_required above the views name that you want to restrict
2.go to project setting.py and LOGIN_URL='which views you want to redirect'
in my case.  LOGIN_URL='login'
"""

# Create your views here.

@login_required
def todolist(request):
    if request.method == "POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manager=request.user # access the login user and manager values set default it
            instance.save()
        messages.success(request,("New Task Added!"))
            
        return redirect('todolist') 
    else:    
        all_tasks=TaskList.objects.filter(manager=request.user).order_by('-created')
        paginator=Paginator(all_tasks,10)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        return render(request,'todolist.html',{'all_tasks':all_tasks})
  

@login_required  
def delete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
        
    else:
        messages.error(request,("Access Restricted,You are not allowed!"))
    
        
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method=="POST":
        task=TaskList.objects.get(pk=task_id) 
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited!"))    
        return redirect('todolist') 
    else:    
        task_obj=TaskList.objects.get(pk=task_id)      
        return render(request,'edit.html',{'task_obj':task_obj})
   
   

@login_required 
def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Access Restricted,You are not allowed!"))
        
    return redirect('todolist')


@login_required
def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done=False
        task.save()
    else:
        messages.error(request,("Access Restricted,You are not allowed!"))
    return redirect('todolist')
    
    
def contract(request):
    context={'Welcome_text':'Welcome to Contract Us App'}
    return render(request,'contract.html',context)

def about(request):
    context={'Welcome_text':'Welcome to About Us App'}
    return render(request,'about.html',context)

def index(request):
    context={'Index_text':'Welcome to Index Page'}
    return render(request,'index.html',context)


