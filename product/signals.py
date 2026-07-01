from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def add_price(sender, instance, created, **kwargs):
    if created:
        if instance.price<50:
            instance.price+=15
            instance.save()
        else:
            instance.price+=10
            instance.save()


