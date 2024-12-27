from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.BeneficiaryList.as_view(), name="home"),
    path('<slug:slug>/', views.beneficiary_detail, name="beneficiary_detail"),
    path('<slug:slug>/slot_edit/<int:slot_id>', views.slot_edit, name="slot_edit"),
    
]
