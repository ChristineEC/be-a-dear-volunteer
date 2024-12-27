from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Beneficiary, Slot
from .forms import SlotForm


class BeneficiaryList(generic.ListView):
    queryset = Beneficiary.objects.filter(status=1).order_by("beneficiary_name")
    template_name = "volunteer/index.html"
    paginate_by = 6


def beneficiary_detail(request, slug):
    """
    Displays an individual :model: `volunteer.Beneficiary`.
    **Context**
    ``beneficiary``
        An instance of :model: `volunteer.Beneficiary`
    ``slots``
        Shows all slots with public_ok=True related
        to the beneficiary.
    ``form``
        An instance of :form: `volunteer.SlotForm`.
    **Template**
        :template:`volunteer/beneficiary_detail.html`
    """

    queryset = Beneficiary.objects.filter(status=1)
    beneficiary = get_object_or_404(queryset, slug=slug)
    slots = beneficiary.slots.all().order_by("-created_on")
    slots_created_count = beneficiary.slots.all().count()
    slots_completed_count = beneficiary.slots.filter(completed=True).count()
    if request.method == "POST":
        form = SlotForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.reserved_by = request.user
            slot.beneficiary = beneficiary
            form.save(slot)
            messages.add_message(
                request, messages.SUCCESS,
                "Your slot has been saved and will now appear"
                "on your personal page." 
                "It will not be shown publicly on this page"
                "unless and until it is approved for publication."
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                "There has been an error. Please ensure you fill out"
                "the date and time field with dates in format YYYY-MM-DD"
                "and times as 00:00:00 only."
            ) 

    form = SlotForm()

    return render(
        request,
        "volunteer/beneficiary_detail.html",
        {
            "beneficiary": beneficiary,
            "slots": slots,
            "slots_created_count": slots_created_count,
            "slots_completed_count": slots_completed_count,
            "form": form,
        },
    )


def slot_edit(request, slug, slot_id):
    """
    View to edit a slot
    """

    if request.method == "POST":

        queryset = Beneficiary.objects.filter(status=1)
        beneficiary = get_object_or_404(queryset, slug=slug)
        slot = get_object_or_404(Slot, pk=slot_id)
        form = SlotForm(request.POST, instance=slot)

        if form.is_valid() and slot.reserved_by == request.user:
            slot = form.save(commit=False)
            slot.beneficiary = beneficiary
            slot.publish_ok = False
            form.save(slot)
            messages.add_message(request, messages.SUCCESS,
                'Your task has been updated!')
        else:
            messages.add_message(request, messages.ERROR,
            'An error occurred updating the task')

    return HttpResponseRedirect(reverse('beneficiary_detail', args=[slug]))



