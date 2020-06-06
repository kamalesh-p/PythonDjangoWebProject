"""
Definition of urls for PythonDjangoWebProject.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # include multiple apps here
    path('',include('app.urls')),
    path('admin/', admin.site.urls),
]
