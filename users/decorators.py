from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps


def not_logged_in():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                messages.warning(
                    request, "You are already logged in, please logout to continue"
                )
                if request.user.isVendor:
                    print("hi")
                    return redirect("marketplace:vendor-dashboard")
                elif request.user.isCustomer:
                    return redirect("marketplace:home")
            return view(request, *args, **kwargs)

        return _wrapped_view

    return decorator
