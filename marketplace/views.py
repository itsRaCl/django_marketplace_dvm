from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, ItemTag
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from .decorators import customer_login_required, vendor_login_required

# from users.models import Customer, Vendor


# Create your views here.
def home(request, *args, **kwargs):
    items = Item.items.get_all_listed()

    for item in items:
        pass
    context = {
        "items": Item.items.get_all_listed(),
    }
    return render(request, "marketplace/home.html", context=context)


@method_decorator(vendor_login_required(), name="dispatch")
class CreateTag(SuccessMessageMixin, CreateView):
    model = ItemTag
    success_message = "Tag created successfully"
    fields = ["tag_name"]

    def get_success_url(self):
        return reverse("marketplace:home")


@method_decorator(vendor_login_required(), name="dispatch")
class CreateItem(SuccessMessageMixin, CreateView):
    model = Item
    success_message = "Item created successfully"
    fields = [
        "item_name",
        "item_quantity",
        "item_price",
        "item_image",
        "item_description",
        "item_tags",
    ]

    def get_success_url(self):
        return reverse("marketplace:add-item")


@vendor_login_required()
def vendor_dashboard(request):
    vendor = request.user
    listed_items = Item.items.get_all_listed(vendor=vendor)

    return render(
        request,
        "marketplace/vendor_dashboard.html",
        {"vendor": vendor, "listed_items": listed_items},
    )
