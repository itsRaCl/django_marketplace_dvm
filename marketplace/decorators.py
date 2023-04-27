from django.contrib import messages
from django.shortcuts import redirect, render
from functools import wraps


def customer_login_required():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(
                    request, "You are not logged in please log in as a customer"
                )
                return redirect(f"login?next={request.path}")
            elif not request.user.isCustomer:
                messages.error(
                    request, "You are not a customer, please log in as a customer"
                )
                return redirect(f"login?next={request.path}")
            return view(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def vendor_login_required():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(
                    request, "You are not logged in please log in as a vendor"
                )
                return redirect(f"login?next={request.path}")
            elif not request.user.isVendor:
                messages.warning(
                    request, "You are not a vendor, please log in as a vendor"
                )
                return redirect(f"login?next={request.path}")
            return view(request, *args, **kwargs)

        return _wrapped_view

    return decorator
