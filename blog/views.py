from django.shortcuts import render
from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    for post in posts:
        post = {
            'title': post.title,
            'timestamp': post.timestamp,
            'body': post.body
        }
    return render(request, 'archive.html')

