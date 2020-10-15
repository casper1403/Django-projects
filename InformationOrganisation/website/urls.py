from django.urls import path
from .views import homeView, showView, bookView, aboutView


urlpatterns = [
    path('', homeView, name='home'),
    path('show/<game>', showView, name='show'),
    path('book/<int:pk>/', bookView, name='book'),
    path('about/', aboutView, name='about'),
]
