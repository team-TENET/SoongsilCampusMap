from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static   
from django.conf import settings

urlpatterns = [
    path('loginFind', loginFind, name="loginFind"),
    path('loginRegister', loginRegister, name="loginRegister"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)