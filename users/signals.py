# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile


# @receiver(pre_save, sender=User)
# def create_profile(sender, created, instance, **kwargs):

#     print("Sender is:", sender)
#     print("Instance is", instance)
#     print("Created is", created)

#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()

    
