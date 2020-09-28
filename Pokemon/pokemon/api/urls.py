
from django.contrib import admin
from django.urls import path
from .views import pokemon_list,generation_list

urlpatterns = [
    path('api/<int:health>/<int:att>', pokemon_list),
    path('api/<generation>',generation_list),
]
