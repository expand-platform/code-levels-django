from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class AdminStaffOnlyMiddleware:
    """
    Middleware to restrict /admin/ access to staff users only.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/cp/'):
            if not request.user.is_authenticated:
                return redirect('/accounts/login/?next=' + request.path)
            if not request.user.is_staff:
                return redirect('/')
        return self.get_response(request)
