from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile



# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Enables specific fields in the display
    of instances of the Slot model
    in the admin panel.
    """
    list_display = (
        'alias',
        'homeroom',
        'class_year'
        )

    search_fields = [
        'homeroom'
    ]
    list_filter = ('homeroom', 'alias')

    class Meta:
        ordering = ['class_year', 'homeroom', 'alias']
    

# Taken from 
# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/

class ProfileInline(admin.StackedInline):
    """
    When a user is created in the admin panel,
    the fields for the Profile model
    also appear so that the superuser ????
    ???Might be wrong here. I think the above
    is done through signals and I thought
    below was for aligning the fields (left side of panel) in the same
    row.????????????????
    """
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"
    list_display = (
        'user',
        'homeroom',
        'class_year'
    )
    search_fields = [
        'homeroom',
        'alias'
    ]

    class Meta:
        ordering = [
            'homeroom',
            'alias'
        ]
    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}, alias {self.alias}, is in homeroom number {self.homeroom.homeroom_number}"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


# Re-register UserAdmin
# admin.site.unregister(Profile)
admin.site.register(Profile)

# admin.site.register(User, UserAdmin)
