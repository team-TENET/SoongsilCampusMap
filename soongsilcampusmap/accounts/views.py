from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def loginFind(request):
    return render(request, "loginFind.html")

def loginRegister(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        auth.login(request, user)
        return render(request, 'home.html')
    else:
        return render(request, 'loginRegister.html')