from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('register',views.regUser,name='register_user')
]