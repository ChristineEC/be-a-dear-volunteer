from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_project, name="about"),
    path("contact_us/", views.send_message, name="send_message"),
]
