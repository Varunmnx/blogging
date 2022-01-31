from multiprocessing import context
from pyexpat import model
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView
# Create your views here.

# def home(request):
#     context={'posts':Post.objects.all()}
#     return render(request,'app1/home.html',context)

class PostListView(ListView):
    model = Post
    template_name= 'app1/home.html'
    ordering =['-date_posted'] 
    context_object_name = 'posts' 
    

class PostDetailView(DetailView):
    model = Post
        

def about(request):
    return render(request,'app1/about.html',{'title':"About"})

