from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static   
from django.conf import settings

urlpatterns = [
    path('common', common, name="common"),
    path('freeBoard', freeBoard, name="freeBoard"),
    path('home', home, name="home"),
    path('infoBoard', infoBoard, name="infoBoard"),
    path('map', map, name="map"),
    path('read/<int:id>', read, name="read"),
    path('read_free/<int:id>', read_free, name="read_free"),
    path('search', search, name="search"),
    path('write', write, name="write"),
    path('create', create, name="create"),
    path('write_free', write_free, name="write_free"),
    path('create_free', create_free, name="create_free"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)