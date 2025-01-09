# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# # from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Profile




# # Create your views here.




# def register_user(request):
#     return render(request, "register.html", {})


# def create_profile(request, instance, created):

#     """
#     Enables a user to enter profile
#     information upon signup.
#     ``user``
#         An instance of :model: accounts.User
#     ``homeroom``
#         An instance of :model: `volunteer.Homeroom`,
#     **Template**
#         :template: `users/profile.html`
#     """
#     print("The function is being called")
#     return HttpResponse(user.username)

#     if request.method == "POST":
#         profile_form = ProfileForm()
#         if profile_form.is_valid():
# )