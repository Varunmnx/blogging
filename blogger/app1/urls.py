from unicodedata import name
from django.urls import path,include

from blogger.settings import DEBUG, MEDIA_ROOT
from . import views 
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView,PostDetailView,PostCreateView

urlpatterns = [
path('profile/',user_views.profile,name='profile'),
path('',PostListView.as_view(),name='blog-home'),
# path('',views.home,name='blog-home'),
path('about/',views.about,name='blog-about'),
path('register/',user_views.register,name='register'),
path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
path('post/new/',PostCreateView.as_view(),name='post-create')


]

if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
