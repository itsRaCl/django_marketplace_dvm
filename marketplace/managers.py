from django.db.models import Manager


class ItemManager(Manager):
    def get_all_listed(self, vendor=None):
        if vendor == None:
            return self.all()
        else:
            return self.filter(vendor=vendor)

    def get_sorted_by(self, price=False, quantity=False, vendor=None):
        if price:
            if vendor == None:
                return self.order_by("item_price").all()
            else:
                return self.order_by("item_price").filter(vendor=vendor)
        elif quantity:
            if vendor == None:
                return self.order_by("item_quantity").all()
            else:
                return self.order_by("item_quantity").filter(vendor=vendor)
