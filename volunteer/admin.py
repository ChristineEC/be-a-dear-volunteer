from django.contrib import admin
from .models import Beneficiary
# from .models import Beneficiary, Slot, Homeroom
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Beneficiary)
class BeneficiaryAdmin(SummernoteModelAdmin):

    """
    BeneficiaryAdmin inherits from SummernoteModelAdmin
    in order to include the summernote field
    enabling formatting the beneficiary description
    in the admin panel.
    """

    list_display = ('beneficiary_name', 'slug', 'status')
    search_fields = ['beneficiary_name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('beneficiary_name',)}
    summernote_fields = ('description',)

    def __str__(self):
        return f"Beneficiary: {self.beneficiary_name}"


# @admin.register(Homeroom)
# class HomeroomAdmin(admin.ModelAdmin):
#     list_display = ("homeroom_number", "class_year")


# # Register your models here.
# @admin.site.unregister(Beneficiary)
# admin.site.register(Slot)
# admin.site.unregister(Beneficiary)
# admin.site.unregister(Slot)
# admin.site.unregister(Homeroom)
