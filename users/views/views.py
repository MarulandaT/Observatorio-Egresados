"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile, Follower

# Forms
from users.forms import SignupForm

# Http
from django.http import HttpResponse
from django.template.loader import get_template

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def post(self, request, *args, **kwargs):
        if 'follow_user' in request.POST:
            id_user = request.POST.get('id_user')
            profile = Profile.objects.filter(pk=id_user)
            if profile.count() != 0:
                follower = Follower(
                    user=request.user.profile,
                    account=profile[0]
                )
                follower.save()
                return redirect('/users/%s/' % profile[0].user)
        elif 'unfollow_user' in request.POST:
            id_user = request.POST.get('id_user')
            profile = Profile.objects.filter(pk=id_user)
            if profile.count() != 0:
                follower = Follower.objects.filter(
                    user=request.user.profile,
                    account=profile[0]
                )
                if follower.count() != 0:
                    follower[0].delete()
                return redirect('/users/%s/' % profile[0].user)

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        profile = Profile.objects.get(user=user)
        context['following'] = Follower.objects.filter(user=self.request.user.profile, account=profile).count() != 0

        return context


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = '/users/login/'

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['city', 'interests', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return '/users/%s/' % username

def login_view(request):
    template = get_template('users/login.html')
    ctx = {
        'show_error': False,
        'message': ''
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            ctx['show_error'] = True
            ctx['message'] = 'Usuario no existe, verifica tus datos'
        else:
            profile = Profile.objects.filter(user=user)
            if profile.count() == 0:
                ctx['show_error'] = True
                ctx['message'] = 'Usuario no existe, verifica tus datos'
            else:
                if user.profile.authorized:
                    login(request, user)
                    return redirect('/')
                elif not user.profile.authorized:
                    ctx['show_error'] = True
                    ctx['message'] = 'Usuario no está autorizado, contacte al administrador'

    return HttpResponse(template.render(ctx, request))


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('/users/login/')
