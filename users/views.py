from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from volunteer.models import Homeroom
from django.http import HttpResponse

# # Create your views here.
def create_profile(request, user):
    print("The function is being called")
    return HttpResponse(user.username)

#     """
#     Creates a profile for a user :model: `users.Profile`
#     **Context**
#     ``user``
#         An instance of :model: accounts.User
#     ``homeroom``
#         An instance of :model: `volunteer.Homeroom`,
#         with ``homeroom_number`` the attribute
#         to be set in the form that is called
#     ``class_year``
#         An attribute of the profile object, to
#         be set automatically set through the form 
#         when homeroom_number is specified(????)
#     **Template**
#         :template: `users/profile.html`
#     """
    
#     if request.method == "GET":
#         profile_form = ProfileForm(data=request.GET)
#         if profile_form.is_valid():


