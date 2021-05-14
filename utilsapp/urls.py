from django.contrib import admin
from django.urls import path, include
from utilsapp import views
from django.shortcuts import render

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
]