from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginPage, name='index'),
    path('signin/', views.LoginPage, name='loginpage'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
