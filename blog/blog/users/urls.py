from django.urls import path,include
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views



app_name = 'users'

urlpatterns = [
    path('register/', user_views.Register , name='Register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name='Logout'),
    path('profile/', user_views.Profile , name='Profile')
]
