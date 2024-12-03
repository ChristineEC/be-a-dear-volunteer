from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    
    list_filter = ('status',)
    summernote_fields = ('content',)

    def __str__(self):
        return self.title