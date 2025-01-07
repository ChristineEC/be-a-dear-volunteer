from django.contrib import admin
from .models import Beneficiary, Slot, Classroom
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Beneficiary)
class BeneficiaryAdmin(SummernoteModelAdmin):

    """
    BeneficiaryAdmin inherits from SummernoteModelAdmin
    in order to include the summernote fiel
    enabling formatting the beneficiary description
    in the admin panel.
    """

    list_display = ( 'beneficiary_name','id', 'location', 'contact_details', 'status')
    search_fields = ['beneficiary_name',]
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('beneficiary_name',)}
    summernote_fields = ('short_description', 'description',)

    class Meta:
        ordering = ['beneficiary_name']


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    """
   Enables specific fields in the display
   of instances of the Slot model
   in the admin panel.
    """
    list_display = (
        'beneficiary',
        'task',
        'task_location',
        'dates',
        'times',
        'reserved_by',
        'credit_minutes_requested',
        'credit_minutes_approved',
        )

    search_fields = []
    list_filter = ('reserved_by',)

    class Meta:
        ordering = ['status', 'reserved_by']


# # Registration of model
admin.site.register(Classroom)
