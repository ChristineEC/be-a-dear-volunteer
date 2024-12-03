from django.shortcuts import render
from .models import About


# # Create your views here.

def about_project(request):
    
    """
    Renders the About page
    """

    about = About.objects.filter(status=1).first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
