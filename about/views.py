from django.shortcuts import render
from .models import AboutProject


# # Create your views here.

def about_project(request):
    """
    Renders the About page
    """


    about = AboutProject.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
