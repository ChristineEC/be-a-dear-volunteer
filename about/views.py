from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm



# # Create your views here.

def about_project(request):
    
    """
    Renders the About page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks for your message! We will '
                'get back to you or implement your '
                'suggestion, if approved, in the '
                'next few days or just as soon '
                'as we can. Have a great day!'
            )
    about = About.objects.filter(status=1).order_by('updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            'collaborate_form': collaborate_form
        },
    )
