"""Defines url patterns for users."""

from django.urls import path, include
from . import views # imports views from current directory

app_name = 'users'
urlpatterns = [
        # Include default auth urls

        # django built in 'login' url already has a built in view for it also. 
        # We still have to build the template though.
        path('', include('django.contrib.auth.urls')),

        # Registration Page
        path('register/', views.register, name='register'),
        ]
