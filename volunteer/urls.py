from . import views
from django.urls import path

urlpatterns = [
    path('', views.BeneficiaryList.as_view(), name="home"),
]
