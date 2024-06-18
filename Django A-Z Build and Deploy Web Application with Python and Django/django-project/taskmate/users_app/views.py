from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm #default for user creation
from .forms import CustomRegisterForm

from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        register_form=CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("Register is Done!"))
            return redirect('register')
    else:   
        register_form=CustomRegisterForm()
    
    return render(request,'register.html',{'register_form':register_form})


