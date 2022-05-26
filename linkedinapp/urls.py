from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('useraccount/', views.useraccount, name='useraccount'),
    path('profile/', views.profile, name='profile'),
    path('userdetail/', views.userdetail, name='userdetail'),
    path('seekerprofile/', views.seekerprofile, name='seekerprofile'),
    path('educationdetail/', views.educationdetail, name='educationdetail'),
    path('experiencedetail/', views.experiencedetail, name='experiencedetail'),
    path('seekerskillset/', views.seekerskillset, name='seekerskillset'),
    path('company/', views.company, name='company'),
    path('jobtype/', views.jobtype, name='jobtype'),
    path('joblocation/', views.joblocation, name='joblocation'),
    path('jobpost/', views.jobpost, name='jobpost'),
    path('joblocation/', views.joblocation, name='joblocation'),
    path('login/', auth_view.LoginView.as_view(template_name='linkedinapp/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='linkedinapp/logout.html'), name="logout"),
]
