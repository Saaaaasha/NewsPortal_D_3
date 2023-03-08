from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import *
from datetime import datetime
from django.http import HttpResponse


# class AuthorsList(ListView):
#     model = Author
#     context_object_name = 'Authors'
#     template_name = 'authors.html'

    # def get_queryset(self):
    #     self.author_user = get_object_or_404(Author, name=self.args[0])
    #     return Author.objects.filter(author_user=self.author_user)


class NewsList(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news.html'
    context_object_name = 'news'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



