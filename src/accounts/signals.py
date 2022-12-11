from django.db.models.signals import post_save
from django.dispatch import receiver

from src.accounts.models import User, Profile


@receiver(post_save, sender=User)
def user_profile_save(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()