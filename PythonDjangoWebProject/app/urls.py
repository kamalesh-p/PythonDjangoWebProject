"""
    urls for app 
"""


from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, views
# change '.' to 'app'


urlpatterns = [
    path('', views.home, name='home'),
]
