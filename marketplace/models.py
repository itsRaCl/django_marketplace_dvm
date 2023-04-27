from django.db import models
from .scripts import get_deleted_user, get_deleted_item
from django.core.validators import MinValueValidator
from django_resized import ResizedImageField
from .managers import ItemManager


# Create your models here.
class ItemTag(models.Model):
    tag_name = models.CharField(verbose_name="Item Tag", max_length=100)

    def __str__(self):
        return self.tag_name

    def get_total_sold(self):
        return sum([x.quantity_sold for x in self.item_set.all()])


class Item(models.Model):
    item_name = models.CharField(verbose_name="Item Name", max_length=100)
    item_quantity = models.PositiveSmallIntegerField(verbose_name="Item Quantity")
    item_price = models.DecimalField(
        verbose_name="Item Price",
        max_digits=19,
        decimal_places=2,
        validators=[
            MinValueValidator(limit_value=0, message="Price cannot be less than zero"),
        ],
    )
    item_image = ResizedImageField(
        verbose_name="Item Image",
        default="item_images/item_default.jpg",
        upload_to="item_images",
        size=[250, None],
        blank=True,
    )
    vendor = models.ForeignKey("users.Vendor", on_delete=models.RESTRICT)
    item_description = models.CharField(verbose_name="Item Description", max_length=255)
    item_tags = models.ManyToManyField(ItemTag, blank=True)
    quantity_sold = models.PositiveIntegerField(verbose_name="Quantity Sold", default=0)
    is_listed = models.BooleanField(verbose_name="Is this item listed?", default=True)
    items = ItemManager()

    def __str__(self):
        return self.item_name


class Order(models.Model):
    customer = models.ForeignKey(
        "users.Customer", on_delete=models.SET(get_deleted_user)
    )
    total_bill_amount = models.DecimalField(
        verbose_name="Bill Amount",
        max_digits=19,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0)],
    )


class OrderedItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.SET(get_deleted_item))
    ordered_quantity = models.PositiveSmallIntegerField(verbose_name="Ordered Quantity")
    price_bought = models.DecimalField(
        verbose_name="Buying Price",
        max_digits=19,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0)],
    )
