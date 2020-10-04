from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('clear_history', views.clear_history, name='clear_history'),
    path('contact', views.contact, name='contact'),
    path('result', views.result, name='result'),
    path('', views.index, name='mainApp'),
]

# python manage.py runserver