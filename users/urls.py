from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.create_profile, name="profile"),
]
