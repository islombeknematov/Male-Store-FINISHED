from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def my_handler(sender, instance, **kwargs):
    if instance.discount:
        instance.real_price = (100 - instance.discount) / 100 * instance.price
    else:
        instance.real_price = instance.price


