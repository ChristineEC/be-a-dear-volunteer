from django.apps import AppConfig
from django.contrib.auth.models import User
from .models import Profile


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    """
    initialization task --
    registering signals (overrides the ready()
    method of the the users app config, or the ability
    to save a user account without creating a profile)
    """
    def ready(self):
        import users.signals   #noqa
