from django.shortcuts import render

def loginFind(request):
    return render(request, "loginFind.html")

def loginRegister(request):
    return render(request, "loginRegister.html")