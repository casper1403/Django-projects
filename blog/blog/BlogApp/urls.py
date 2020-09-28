from django.urls import path,include
from . import views
from BlogApp.views import IndexView, PostListView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView, LandingView

app_name = 'BlogApp'

urlpatterns = [
    path('', LandingView.as_view(), name='Landing'),
    path('home/', IndexView.as_view(), name='Index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post-detail'),
    path('chapters/new/', PostCreateView.as_view(), name='Post-create'),
    path('chapters/', PostListView.as_view() , name='Blogs'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Post-delete'),
]
