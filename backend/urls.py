
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('video',views.videoupload,name="video"),
    path('videoprocess',views.videoprocess,name="videoProcess"),
]
