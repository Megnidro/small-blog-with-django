from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "blog/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "blog/detail.html"
