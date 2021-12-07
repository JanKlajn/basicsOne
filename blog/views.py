from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    ctx = {
        'posts': posts
    }
    return TemplateResponse(request, 'archive.html', ctx)


def archive1(request):
    posts = BlogPost.objects.all()
    ctx = {
        'posts': posts
    }
    return render(request, 'archive1.html', ctx)


