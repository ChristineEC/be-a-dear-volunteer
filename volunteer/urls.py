from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.BeneficiaryList.as_view(), name="home"),
    path('<slug:slug>/', views.beneficiary_detail, name="beneficiary_detail")
    
]
