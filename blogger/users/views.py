from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from importlib_metadata import email
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
   
    if request.method =='POST':
        form =UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            email= form.cleaned_data.get('email')
            messages.success(request,f'Your account has been created !! Now you can login')
            return redirect('login')   
        else:
            messages.warning(request,f'invalid credentials')       
    else:
        form =UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})

@login_required()
def profile(request):
    return render(request,'users/profile.html')    