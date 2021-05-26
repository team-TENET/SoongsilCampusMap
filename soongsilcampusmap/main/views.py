from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def common(request):
    return render(request, 'common.html')

def freeBoard(request):
    return render(request, 'freeBoard.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def infoBoard(request):
    return render(request, 'infoBoard.html')

def map(request):
    return render(request, 'map.html')

def read(request):
    return render(request, 'read.html')

def search(request):
    return render(request, 'search.html')

def write(request):
    return render(request, 'write.html')

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