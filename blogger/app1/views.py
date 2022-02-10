from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from unicodedata import name
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User 
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

# def home(request):
#     context={'posts':Post.objects.all()}
#     return render(request,'app1/home.html',context)

class PostListView(ListView):
    model = Post
    template_name= 'app1/home.html'
    ordering =['-date_posted'] 
    context_object_name = 'posts'
    paginate_by = 3
    

#user based postings 
class UserPostListView(ListView):
    model = Post
    template_name= 'app1/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


#userbased postings end    

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content'] 
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)    


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content'] 
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        



def about(request):
    return render(request,'app1/about.html',{'title':"About"})

#i added this