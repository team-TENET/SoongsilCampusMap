from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('loginFind', loginFind, name="loginFind"),
    path('loginRegister', loginRegister, name="loginRegister"),

]