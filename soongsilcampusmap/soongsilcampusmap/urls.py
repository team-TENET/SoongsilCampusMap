"""soongsilcampusmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import *
from main.views import *
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('common', common, name="common"),
    path('freeBoard', freeBoard, name="freeBoard"),
    path('index', index, name="index"),
    path('infoBoard', infoBoard, name="infoBoard"),
    path('map', map, name="map"),
    path('post', post, name="post"),
    path('search', search, name="search"),
    path('write', write, name="write"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
