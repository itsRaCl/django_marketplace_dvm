from django.urls import path
import users.views as user_views
import django.contrib.auth.views as auth_views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("vendor-login/", user_views.vendor_login, name="vendor-login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"),
        name="passwd-reset",
    ),
    path(
        "password-reset-form",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/reset_password_form.html"
        ),
        name="passwrd-reset-conf",
    ),
    path("customer-register/", user_views.customer_register, name="customer-register"),
    path("vendor-register/", user_views.vendor_register, name="vendor-register"),
    path(
        "create-vendor-profile",
        user_views.create_vendor_profile,
        name="create-vendor-profile",
    ),
]
