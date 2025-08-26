from django.shortcuts import redirect
from django.urls import reverse

WHITELIST_PREFIXES = (
    '/static/',            # static files
    '/admin/login/',       # admin login page
    '/health/',            # optional health check
)

def is_whitelisted(path):
    if path in (reverse('user_login'),):   # your login view
        return True
    return any(path.startswith(p) for p in WHITELIST_PREFIXES)

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if not request.user.is_authenticated and not is_whitelisted(request.path):
            return redirect('user_login')
        return self.get_response(request)
