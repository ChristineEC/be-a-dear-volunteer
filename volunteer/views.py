from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Beneficiary, Slot
from .forms import SlotForm
from .forms import SlotUpdateForm


class BeneficiaryList(generic.ListView):
    queryset = Beneficiary.objects.filter(status=1).order_by("beneficiary_name")
    template_name = "volunteer/index.html"
    paginate_by: 6


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


def slot_edit(request, slot_id):
    """
    View to edit a slot from the student dashboard
    """
    # if request.method == "GET":
    #     user = request.user
    #     slot = get_object_or_404(Slot, pk=slot_id)
    #     update_form = SlotUpdateForm(request.POST, instance=slot)

    if request.method == "POST":
        user=request.user
        slot = get_object_or_404(Slot, pk=slot_id)
        update_form = SlotUpdateForm(request.POST, instance=slot)
        if update_form.is_valid() and slot.reserved_by == request.user:
            slot = update_form.save(commit=False)
            slot.beneficiary = beneficiary
            slot.publish_ok = False
            slot.save()
            messages.add_message(request, messages.SUCCESS,
                'Your task has been updated!')
        else:
            messages.add_message(request, messages.ERROR,
            'An error occurred updating the task')

    update_form = SlotUpdateForm()

    return render(
        response, 
        'volunteer/student/student_dashboard.html',
        {
            'slot_id':slot_id,
            'slot': slot,
            'update_form': update_form,},
        )


@login_required(redirect_field_name="account_login")
def student_dashboard(request):
    """
    Renders the student dashboard page.
    """
    queryset = Beneficiary.objects.filter(status=1)
    user = request.user
    slots = Slot.objects.filter(reserved_by=user)

    return render(
        request,
        "volunteer/student_dashboard.html",
        {"slots": slots,}
    )

