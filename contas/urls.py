from django.urls import path
from contas import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('', views.register, name='registro'), 
] 