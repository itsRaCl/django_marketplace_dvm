from django.db.models.signals import post_save
from .models import Customer, Vendor, CustomerProfile, VendorProfile
from django.dispatch import receiver


@receiver(post_save, sender=Customer)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(customer=instance)


@receiver(post_save, sender=Customer)
def save_profile(sender, instance, **kwargs):
    instance.customerprofile.save()


@receiver(post_save, sender=Vendor)
def create_profile(sender, instance, created, **kwargs):
    if created:
        VendorProfile.objects.create(vendor=instance)


@receiver(post_save, sender=Vendor)
def save_profile(sender, instance, **kwargs):
    instance.vendorprofile.save()
