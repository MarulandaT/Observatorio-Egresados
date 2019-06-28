"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture:
                    if request.path not in ['/users/me/profile/', '/users/logout/']:
                        return redirect('/users/me/profile/')

        response = self.get_response(request)
        return response

class UserAuthorizedMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            from users.models import Profile

            if Profile.objects.filter(user=request.user).count() != 0:
                profile = request.user.profile
                if not profile.authorized:
                    from django.contrib.auth import logout
                    logout(request)
                    return redirect('/users/login/')

        response = self.get_response(request)
        return response
