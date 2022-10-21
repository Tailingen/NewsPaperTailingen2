from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'

class NewDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'new'
