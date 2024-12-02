from django.shortcuts import render
from django.views import generic
from .models import Beneficiary

# Create your views here.
class BeneficiaryList(generic.ListView):
    queryset = Beneficiary.objects.all()
    template_name = "beneficiary_list"
