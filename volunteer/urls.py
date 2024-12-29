from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.BeneficiaryList.as_view(), name="home"),
    path('student/', views.student_dashboard, name="student_dashboard"),
    path('<slug:slug>/', views.beneficiary_detail, name="beneficiary_detail"),
    path('<slug:slug>/edit_slot/<int:slot_id>', views.slot_edit, name="slot_edit"),
]
