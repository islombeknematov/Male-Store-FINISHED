from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import ProfileModel, UserModel


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, **kwargs):
    if not hasattr(instance, 'profile'):
        ProfileModel.objects.create(user=instance)


