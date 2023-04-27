from django.contrib import admin
from .models import Item, Order, OrderedItem, ItemTag

# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(ItemTag)
