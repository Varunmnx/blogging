from unicodedata import name
from django.urls import path,include
from app1.models import Post

from blogger.settings import DEBUG, MEDIA_ROOT
from . import views 
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
path('profile/',user_views.profile,name='profile'),
path('',PostListView.as_view(),name='blog-home'),
path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
# path('',views.home,name='blog-home'),
path('about/',views.about,name='blog-about'),
path('register/',user_views.register,name='register'),
path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
path('post/new/',PostCreateView.as_view(),name='post-create'),
path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
  path('password-reset',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),


]

if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
