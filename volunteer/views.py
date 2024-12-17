from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .models import Beneficiary, Slot
from .forms import SlotForm


# Create your views here.

class BeneficiaryList(generic.ListView):
    queryset = Beneficiary.objects.filter(status=1)
    template_name = "volunteer/index.html"
    paginate_by = 2
    
    class Meta:
        ordering = ["beneficiary_name"]


def beneficiary_detail(request, slug):
    """
    Displays an individual :model: `volunteer.Beneficiary`.
    **Context**
    ``beneficiary``
        An instance of :model: `volunteer.Beneficiary`
    ``slots``
        Shows all slots with public_ok=True related
        to the beneficiary.
    ``slot_form``
        An instance of :form: `volunteer.SlotForm`.
    **Template**
        :template:`volunteer/volunteer_detail.html`
    """

    queryset = Beneficiary.objects.filter(status=1)
    beneficiary = get_object_or_404(queryset, slug=slug)
    slots = beneficiary.slots.filter(publish_ok=True).order_by("-created_on")
    slots_created_count = beneficiary.slots.all().count()
    slots_completed_count = beneficiary.slots.filter(completed=True).count()
    if request.method == "POST":
        slot_form = SlotForm(data=request.POST)
        if slot_form.is_valid():
            slot.reserved_by = request.user
            slot.beneficiary = beneficiary
            slot.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your slot has been created and reserved for you." 
                "It will not be shown publicly on this"
                "page until it is approved for publication. Be"
                "be aware that teachers and administrators"
                "can see the slot as soon as it is created."
            )

    slot_form = SlotForm()

    return render(
        request,
        "volunteer/beneficiary_detail.html",
        {
            "beneficiary": beneficiary,
            "slots": slots,
            "slots_created_count": slots_created_count,
            "slots_completed_count": slots_completed_count,
            "slot_form": slot_form,
        },
    )



