from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('common', common, name="common"),
    path('freeBoard', freeBoard, name="freeBoard"),
    path('home', home, name="home"),
    path('infoBoard', infoBoard, name="infoBoard"),
    path('map', map, name="map"),
    path('read', read, name="read"),
    path('search', search, name="search"),
    path('write', write, name="write"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),

]