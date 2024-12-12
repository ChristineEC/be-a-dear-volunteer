from django.contrib import admin
from .models import Beneficiary
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Beneficiary)
# class BeneficiaryAdmin(SummernoteModelAdmin):

#     list_display = ('beneficiary_name', 'slug', 'status')
#     search_fields = ['beneficiary_name']
#     list_filter = ('status',)
#     prepopulated_fields = {'slug': ('beneficiary_name',)}
#     summernote_fields = ('description',)

#     def __str__(self):
#         return self.beneficiary_name



# # Register your models here.

# @admin.register(Homeroom)
# class HomeroomAdmin(admin.ModelAdmin):
#     list_display = ("homeroom_number", "class_year")
    
#     class Meta:
#         ordering = ["class_year", "homeroom_number"]

    
