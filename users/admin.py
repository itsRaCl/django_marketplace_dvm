from django.contrib import admin
from .models import (
    CustomUser,
    Customer,
    Vendor,
    CustomerProfile,
    VendorProfile,
    CustomerAddress,
)

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(CustomerProfile)
admin.site.register(VendorProfile)
admin.site.register(CustomerAddress)
