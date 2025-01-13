from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import About
from .forms import CollaborateForm


def about_project(request):
    """
    Renders the About page
    **Context**
    'collaborate_form`
    an instance of :form: CollaborateForm
    When posted, the form creates
    an instance of :model: CollaborateRequest
    `about`
    an instance of :model: About
    **Template**
    "about/about.html"
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
    about = About.objects.filter(status=1).order_by(
            'updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            'collaborate_form': collaborate_form
        },
    )


def send_message(request):
    """
    Enables a user to send a message
    from the login page if they've
    forgotten their username.
    **Context**
   'collaborate_form`
    an instance of :form: CollaborateForm
    When posted, the form creates
    an instance of :model: CollaborateRequest
    **Template**
    'about/contact_form.html'
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks for your message! We will '
                'get back to you just as soon '
                'as we can. Have a great day!'
            )
            return HttpResponseRedirect('/')

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/contact_form.html",
        {'collaborate_form': collaborate_form},
    )
