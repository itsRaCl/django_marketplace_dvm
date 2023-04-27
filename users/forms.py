from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Vendor, CustomerProfile, VendorProfile, CustomerAddress


class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField()

    field_order = ["email", "password1", "password2"]

    class Meta:
        model = Customer
        fields = {"email", "password1", "password2"}


class VendorCreationForm(UserCreationForm):
    email = forms.EmailField()

    field_order = ["email", "password1", "password2"]

    class Meta:
        model = Vendor
        fields = {"email", "password1", "password2"}


class CustomerUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Customer
        fields = ["email"]


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ["profile_pic", "first_name", "last_name"]


class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        fields = ["address"]


class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = [
            "profile_pic",
            "business_name",
            "business_address",
            "business_contact",
        ]


class CustomerBalanceChangeForm(forms.ModelForm):
    pass


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
