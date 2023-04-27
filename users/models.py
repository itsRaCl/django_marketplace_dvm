from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager, CustomerManager, VendorManager


# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email Address", max_length=255, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    isCustomer = models.BooleanField(default=False)
    isVendor = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Customer(CustomUser):
    objects = CustomerManager()

    class Meta:
        proxy = True

    def save(self):
        if not self.id or self.id == None:
            self.isCustomer = True
            self.isVendor = False
            return super().save()


class CustomerProfile(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    profile_pic = models.ImageField(
        default="profile_pics/default.jpg", upload_to="profile_pics"
    )
    balance = models.DecimalField(
        verbose_name="Customer Wallet Balance",
        decimal_places=2,
        max_digits=19,
        default=0,
        validators=[MinValueValidator(limit_value=0)],
    )

    def __str__(self):
        return f"{self.customer.email}'s Profile"


class CustomerAddress(models.Model):
    address = models.TextField(verbose_name="Customer Address", max_length=2047)
    customer = models.ForeignKey("CustomerProfile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address}"


class Vendor(CustomUser):
    objects = VendorManager()

    class Meta:
        proxy = True

    def save(self):
        if not self.id or self.id == None:
            self.isCustomer = False
            self.isVendor = True
            return super().save()


class VendorProfile(models.Model):
    vendor = models.OneToOneField("Vendor", on_delete=models.CASCADE)
    business_name = models.CharField(verbose_name="Business Name", max_length=255)
    profile_pic = models.ImageField(
        default="profile_pics/default.jpg", upload_to="profile_pics"
    )
    business_address = models.TextField(
        verbose_name="Business Address", max_length=2047
    )
    business_contact = PhoneNumberField(verbose_name="Contact Number", blank=False)

    def __str__(self):
        return f"{self.vendor.email}'s profile"
