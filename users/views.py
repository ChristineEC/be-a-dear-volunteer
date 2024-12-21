from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from volunteer.models import Homeroom
from django.http import HttpResponse
from .forms import ProfileForm

# # Create your views here.
def create_profile(request, user):
    print("The function is being called")
    return HttpResponse(user.username)

    """
    Creates a profile for a user :model: `users.Profile`
    **Context**
    ``user``
        A unique instance of :model: accounts.User
    ``homeroom``
        An instance of :model: `volunteer.Homeroom``
        to be set in the form that is called
    ``profile_pic``
        Allows a user to upload a photo to
        their profile.
    **Template**
        :template: `users/profile.html`
    """
    
    queryset = User.objects.all()
    user = get_object_or_404(queryset, user_id=user_id)
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile.user = request.user  # do I still need this, since it is included in the signal???
            profile.homeroom = Homeroom
            # profile.profile_pic = 
        profile_form.save()
        messages.add_message(
            request, message.SUCCESS,
            "Your profile has been created"
            )

    return redirect(
        "volunteer/index.html"
    )
