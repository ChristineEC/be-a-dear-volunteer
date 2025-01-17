from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('student_dashboard/', views.student_dashboard,
         name="student_dashboard"),
    path('student_dashboard/delete_task/<int:slot_id>/',
         views.delete_via_dashboard, name='delete_via_dashboard'),
    path('<slug:slug>/', views.beneficiary_detail,
         name="beneficiary_detail"),
    path('<slug:slug>/edit_slot/<int:slot_id>/',
         views.slot_edit, name="slot_edit"),
    path('<slug:slug>/delete_slot/<int:slot_id>/',
         views.slot_delete, name="slot_delete"),
    path('update_task/<int:pk>/',
         views.update_slot, name="update_slot"),
    path('volunteer/volunteer_opportunities/', views.BeneficiaryList.as_view(),
         name="beneficiaries"),
]
