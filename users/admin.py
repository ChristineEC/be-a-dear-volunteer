from django.contrib import admin
from .models import Profile, Homeroom

# Register your models here.
# admin.site.register(Homeroom)
admin.site.register(Profile)

@admin.register(Homeroom)
class HomeroomAdmin(admin.ModelAdmin):
    list_display = ("room_num", "class_year")
    ordering = ("room_num",)

