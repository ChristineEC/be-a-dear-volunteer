from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Floor, Mod
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Beneficiary, Slot, Classroom
from .forms import SlotForm



class BeneficiaryList(generic.ListView):
    queryset = Beneficiary.objects.filter(status=1).order_by("beneficiary_name")
    template_name = "volunteer/index.html"
    paginate_by: 6


# Adapted from Code Institute lesson, I Think Therefore I Blog
def beneficiary_detail(request, slug):
    """
    Displays an individual of :model: `volunteer.Beneficiary`.
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
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your slot has been saved and will now appear"
                " on your personal page."
                " It will not be shown publicly on this page"
                " unless and until it is approved for publication."
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

# Adapted from Code Institute lesson, I Think Therefore I Blog
def slot_edit(request, slug, slot_id):
    """
    View to edit a slot directly on the
    beneficiary_detail page.
    **Context**
    `slot`
        An instance of :model: Slot
    ``form``
        An instance of :form: `volunteer.SlotForm`.
    **Template**
        :template:`volunteer/beneficiary_detail.html`
    """
    if request.method == "POST":
        queryset = Beneficiary.objects.filter(status=1)
        beneficiary = get_object_or_404(queryset, slug=slug)
        slot = get_object_or_404(Slot, pk=slot_id)
        slot_form = SlotForm(request.POST, instance=slot)
        if slot_form.is_valid():
            slot = slot_form.save(commit=False)
            slot.beneficiary = beneficiary
            slot.publish_ok = False
            slot.save()
            messages.add_message(request, messages.SUCCESS,
                'Your task has been updated!')

        else:
            messages.add_message(request, messages.ERROR,
            'An error occurred updating the task')

    return HttpResponseRedirect(
        reverse('beneficiary_detail', args=[slug]))

# Adapted from Code Institute lesson, I Think Therefore I Blog
def slot_delete(request, slug, slot_id):
    """
    View to delete a slot directly on the
    beneficiary_detail page.
    **Context**
    `slot`
        An instance of :model: Slot
    **Template**
        :template:`volunteer/beneficiary_detail.html`
    """
    queryset = Beneficiary.objects.filter(status=1)
    beneficiary = get_object_or_404(queryset, slug=slug)
    slot = get_object_or_404(Slot, pk=slot_id)
    if slot.reserved_by == request.user:
        slot.delete()
        messages.add_message(request, messages.SUCCESS,
        'Your task has been deleted!')
    else:
        messages.add_message(request, messages.ERROR,
        'You can only delete your own tasks.')

    return HttpResponseRedirect(
        reverse('beneficiary_detail', args=[slug]))


def update_slot(request, pk):
    """
    View to update a slot from the student dashboard.
    **Context:**
    `slot`
    An instance of :model: Slot
    `form` 
    An instance of :form: volunteer.SlotForm
    ""Template"
    :template: 'volunteer.update_task.html'
    """

    slot = Slot.objects.get(id=pk)
    form = SlotForm(instance=slot)
    user = request.user
    if request.method == "POST":
        form = SlotForm(request.POST, instance=slot)
        if form.is_valid():
            form.save(commit=False)
            slot.publish_ok = False
            slot.save()
            return HttpResponseRedirect(
                reverse('student_dashboard'))
                

    return render(request,
        'volunteer/update_task.html',
        {
            'form': form, 
            'user':user, 
            'slot':slot,
        },
    )


@login_required
def student_dashboard(request):
    """
    Renders the student dashboard page.
    **Context**
    ``user``
        an instance of :model: User
    ``slot``
        an instance of :model: Slot
    **Template**
    'student_dashboard.html'
    
    """
    if request.method == "GET":
        user = request.user
        queryset = Slot.objects.all()
        slots = Slot.objects.filter(reserved_by=user)
        # if slots:
        #     for slot in slots:
        #         if slot.credit_minutes_approved:
        #             slot.credit_minutes_approved = slot.credit_minutes_approved
        #             total_minutes_approved = slots.credit_minutes_approved.sum()
        #             remaining_minutes_required = 1800 - total_minutes_approved
        #             hours_remaining = Floor(remaining_minutes_required/60)
        #             plus_minutes = Mod("remaining_minutes_required", 60)
                
        # else:
        #     slot.credit_minutes_approved = 0
        #     total_minutes_approved = 0
        #     remaining_minutes_required = 1800
        #     hours_remaining = 30
        #     plus_minutes = 0

    return render(
        request,
        "volunteer/student_dashboard.html",
        {"slots": slots,
        # "total_minutes_approved":total_minutes_approved,
        # "remaining_minutes_required":remaining_minutes_required,
        # "hours_remaining":hours_remaining,  
        # "plus_minutes":plus_minutes, 
        }
    )

def delete_via_dashboard(request, pk):
    slot = Slot.objects.get(id=pk)
    if slot.reserved_by == request.user:
        slot.delete()
        messages.add_message(request, messages.SUCCESS,
        'Your task has been deleted!')
    else:
        messages.add_message(request, messages.ERROR,
        'You can only delete your own tasks.')

    return HttpResponseRedirect(
                reverse('student_dashboard'))
