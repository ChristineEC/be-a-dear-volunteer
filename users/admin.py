from django.contrib import admin
from .models import Homeroom, Profile

# Register your models here.
# admin.site.register(Homeroom)
admin.site.register(Profile)

@admin.register(Homeroom)
class HomeroomAdmin(admin.ModelAdmin):
    list_display = ("homeroom_number", "class_year")
    ordering = ("homeroom_number",)

