from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import (
    CustomerCreationForm,
    VendorCreationForm,
    VendorProfileForm,
    LoginForm,
)
from .decorators import not_logged_in


# Create your views here.
@not_logged_in()
def customer_register(request):
    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            messages.add_message(
                request, messages.SUCCESS, "You have been registered in successfully!"
            )
            return redirect("marketplace:home")
        else:
            print(form.errors)
            return HttpResponse("Error!")
    else:
        form = CustomerCreationForm()
        return render(request, "users/customer-register.html", {"form": form})


@not_logged_in()
def vendor_register(request):
    if request.method == "POST":
        form = VendorCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            messages.add_message(
                request, messages.SUCCESS, "You have been registered in successfully!"
            )
            return redirect("marketplace:home")
        else:
            return render(request, "users/vendor-register.html", {"form": form})
    else:
        form = VendorCreationForm()
        return render(request, "users/vendor-register.html", {"form": form})


def create_vendor_profile(request):
    if request.method == "POST":
        form = VendorProfileForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = VendorProfileForm()
        return render(request, "users/profile_create.html", {"form": form})


@not_logged_in()
def vendor_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    return HttpResponse("Blah")
