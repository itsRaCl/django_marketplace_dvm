from django.urls import path
from . import views

app_name = "marketplace"

urlpatterns = [
    path("", view=views.home, name="home"),
    path("add-item", view=views.CreateItem.as_view(), name="add-item"),
    path(
        "add-tag",
        view=views.CreateTag.as_view(),
        name="add-tag",
    ),
    path("vendor-dashboard", view=views.vendor_dashboard, name="vendor-dashboard"),
]
