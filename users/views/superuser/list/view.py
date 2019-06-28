from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def view(request):
    if request.user.profile.type_user != 'superadmin':
        return redirect('/')

    from users.models import Profile

    admins = Profile.objects.filter(type_user='admin')

    template = get_template('superuser/list_users.html')
    ctx = {
        'admins': admins
    }

    return HttpResponse(template.render(ctx, request))
