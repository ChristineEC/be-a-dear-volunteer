# from django.shortcuts import render
# from django.contrib.auth.models import User
# from volunteer.models import Homeroom
# from .models import Profile
# from django.http import HttpResponse


# # # Create your views here.
# def create_profile(request, user):
#     print("The function is being called")
#     return HttpResponse(user.username)

#     """
#     Creates a profile for the user.
#     ``user``
#         An instance of :model: accounts.User
#     ``homeroom``
#         An instance of :model: `volunteer.Homeroom`,
#     **Template**
#         :template: `users/profile.html`
#     """
    
#     if request.method == "GET":
#         profile_form = ProfileForm(data=request.GET)
#         if profile_form.is_valid():
# )