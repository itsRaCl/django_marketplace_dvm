from django.contrib.auth import get_user_model
import marketplace.models


def get_deleted_user():
    return get_user_model().objects.get_or_create(email="<<DELETED>>@<<DELETED>>.com")[
        0
    ]


def get_deleted_item():
    x = marketplace.models.Item()
    return x.objects.get_or_create(item_name="<<DELETED ITEM>>")
