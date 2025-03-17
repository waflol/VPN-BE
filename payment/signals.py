from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from payment.models import Subscription


@receiver(pre_save, sender=Subscription)
def create_final_save(sender, instance, **kwargs):
    instance.final_price = instance.price * (1 - instance.discount / 100)
