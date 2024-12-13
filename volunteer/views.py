from django.shortcuts import render
from django.views import generic
from .models import Beneficiary

# Create your views here.

class BeneficiaryList(generic.ListView):
    queryset = Beneficiary.objects.filter(status=1)
    template_name = "volunteer/index.html"

    # paginate_by = 6

    # class Meta:
    #     ordering = ["-updated_on"]
