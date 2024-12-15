from django.contrib import admin
from .models import Beneficiary
from .models import Slot
# from .models import Homeroom
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Beneficiary)
class BeneficiaryAdmin(SummernoteModelAdmin):

    """
    BeneficiaryAdmin inherits from SummernoteModelAdmin
    in order to include the summernote field
    enabling formatting the beneficiary description
    in the admin panel.
    """

    list_display = ('id', 'beneficiary_name', 'location', 'contact_details', 'status')
    search_fields = ['beneficiary_name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('beneficiary_name',)}
    summernote_fields = ('description',)

    class Meta:
        ordering = ['status', 'beneficiary_name']
    
    def __str__(self):
        return f"Beneficiary: {self.beneficiary_name}"


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):

    """
    TaskAdmin inherits from SummernoteModelAdmin
    in order to include the summernote field
    enabling formatting the beneficiary description
    in the admin panel.
    """

    list_display = (
        'task',
        'task_location',
        'reserved_by',
        'credit_minutes_requested',
        'teacher_approved'
        )
    search_fields = []
    list_filter = ('reserved_by',)
    prepopulated_fields = {'slug': ('task',)}

    class Meta:
        ordering = ['status', 'reserved_by']
    
    def __str__(self):
        return f"Task: {self.task} | Reserved by: {self.reserved_by}"

# @admin.register(Homeroom)
# class HomeroomAdmin(admin.ModelAdmin):
#     list_display = ("homeroom_number", "class_year")


# # Register your models here.


