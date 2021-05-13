from django.shortcuts import render

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

def post(request):
    return render(request, 'post.html')

def search(request):
    return render(request, 'search.html')

def write(request):
    return render(request, 'write.html')
