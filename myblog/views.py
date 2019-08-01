from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(requests):
    posts = Post.objects.all()
    return render(requests, 'index.html', {'posts' : posts})

def post(requests, slug):
    print (slug)
    return render_to_response('post.html', {
        'post' : get_object_or_404(Post, slug=slug)
    })

def about(requests):
    return render(requests, 'about.html', {})