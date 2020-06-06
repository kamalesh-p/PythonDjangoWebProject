"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

# connect html pages in this py file

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/HTML.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
