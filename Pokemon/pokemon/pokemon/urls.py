from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trainer.urls')),
    path('', include('login.urls')),
    path('', include('catch.urls')),
    path('', include('hunt.urls')),
    path('', include('clans.urls')),
    path('', include('api.urls')),
]
