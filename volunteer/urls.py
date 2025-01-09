from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.BeneficiaryList.as_view(), name="home"),
    path('student_dashboard/', views.student_dashboard, name="student_dashboard"),
    path('delete_task/<int:pk>/', views.delete_via_dashboard, name='delete_via_dashboard'),
    path('<slug:slug>/', views.beneficiary_detail, name="beneficiary_detail"),
    path('<slug:slug>/edit_slot/<int:slot_id>/', views.slot_edit, name="slot_edit"),
    path('<slug:slug>/delete_slot/<int:slot_id>/', views.slot_delete, name="slot_delete"),
    path('update_task/<int:pk>/', views.update_slot, name="update_slot")
]
