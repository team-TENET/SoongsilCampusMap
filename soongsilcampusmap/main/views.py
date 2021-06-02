from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post, Post_free
from django.utils import timezone

def common(request):
    return render(request, 'common.html')

def freeBoard(request):
    posts_free = Post_free.objects.all()
    return render(request, 'freeBoard.html', {'posts_free':posts_free})

def home(request):
    posts = Post.objects.all()
    posts_free = Post_free.objects.all()
    return render(request, 'home.html', {'posts':posts, 'posts_free':posts_free})
    # return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def infoBoard(request):
    posts = Post.objects.all()
    return render(request, 'infoBoard.html', {'posts':posts})

def map(request):
    return render(request, 'map.html')

def read(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'read.html', {'post':post})

def read_free(request, id):
    post_free = get_object_or_404(Post_free, pk=id)
    return render(request, 'read_free.html', {'post_free':post_free})

def search(request):
    return render(request, 'search.html')

def write(request):
    return render(request, 'write.html')

def create(request):
    new_post=Post()
    new_post.title=request.POST['title']
    new_post.body=request.POST['body']
    new_post.pub_date= timezone.now()
    new_post.author=request.user
    new_post.save()
    return redirect('infoBoard')

def write_free(request):
    return render(request, 'write_free.html')

def create_free(request):
    free_post=Post_free()
    free_post.title=request.POST['title']
    free_post.body=request.POST['body']
    free_post.pub_date= timezone.now()
    free_post.author=request.user
    free_post.save()
    return redirect('freeBoard')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html', {'error' : 'username or password is incorrect. '})

    else:
        return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')