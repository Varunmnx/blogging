from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.template import context
from django.urls import is_valid_path
from importlib_metadata import email

from app1.views import home
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,UserUpdateForm
# Create your views here.
def register(request):
   
    if request.method =='POST':
        form =UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username= form.cleaned_data.get('username')
            # email= form.cleaned_data.get('email')
            messages.success(request,f'Your account has been created !! Now you can login')
            return redirect('login')   
        else:
            messages.warning(request,f'invalid credentials')       
    else:
        form =UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})

@login_required()
def profile(request):
    if request.method == 'POST':
       u_form = UserUpdateForm(request.POST,instance = request.user)
       P_form = ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
       
       if u_form.is_valid() and P_form.is_valid(): 
                  u_form.save()
                  P_form.save()
                  messages.success(request,f'Your account has been updated!!')
                  return redirect('blog-home')
    else:   
            u_form = UserUpdateForm(instance = request.user)
            P_form = ProfileUpdateForm(instance= request.user.profile) 


    context ={
        'u_form': u_form,
        'p_form': P_form
    }
    return render(request,'users/profile.html',context)    