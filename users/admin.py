from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Enabes specific fields of the 
    Profile model to show
    in the admin panel
    """
    list_display = (
        'profile_type',
        'alias',
        'classroom',
    )

    search_fields = [
        'classroom',
        'profile_type',
        'alias',
    ]

    list_filter = ('classroom', 'profile_type', 'alias',)

    class Meta:
        ordering = ['classroom', 'profile_type', 'alias',]

    def __str__(self):
        return f"Alias {self.alias}, is in classroom number {self.classroom}"

class ProfileInline(admin.StackedInline):
    """
    To ensure that, When a user is created
    in the admin panel, the fields for the 
    Profile model also appear so that the
    Profile fields can be updated at the 
    same time.
    """
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"

    
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Site)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
