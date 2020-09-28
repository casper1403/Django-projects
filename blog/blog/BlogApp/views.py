from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import datetime
# Create your views here.


# view of the landingspage
class LandingView(TemplateView):
    template_name = "BlogApp/landing.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LandingView, self).get_context_data(*args, **kwargs)
        context['time'] = datetime.datetime.now()
        return context

class IndexView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = "BlogApp/index.html"
    ordering = ['-date_posted']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset =  BlogPost.objects.filter(author__exact=self.request.user)
            return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['time'] = datetime.datetime.now()
        return context



class PostListView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = "BlogApp/blogs.html"
    ordering = ['-date_posted']



class PostDetailView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Comment
    template_name = "BlogApp/post_detail.html"
    fields = ['comment']


    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['posted'] = BlogPost.objects.get(id=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(post__exact=context['posted'])
        return context


    def form_valid(self, form,  *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.post = BlogPost.objects.get(id=self.kwargs['pk'])
        obj.save()
        return super().form_valid(form)



class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = BlogPost
    template_name = "BlogApp/post_form.html"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = "BlogApp/post_confirm_delete.html"
    success_url = "/home/"

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login/'
    model = BlogPost
    template_name = "BlogApp/post_form.html"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False
