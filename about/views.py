from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


# # Create your views here.

def about_project(request):
    
    """
    Renders the About page
    """

    about = About.objects.filter(status=1).last()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            'collaborate_form': collaborate_form
        },
    )
