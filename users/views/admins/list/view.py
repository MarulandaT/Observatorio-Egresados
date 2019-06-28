from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def view(request):
    if request.user.profile.type_user not in ['admin', 'superadmin']:
        return redirect('/')

    from users.models import Profile

    if request.method == 'POST' and 'authorize_user' in request.POST:
        id_profile = request.POST.get('id_profile')
        profile = Profile.objects.filter(pk=id_profile)
        if profile.count() != 0:
            profile = profile[0]
            profile.authorized = True
            profile.save()

    if request.method == 'POST' and 'deauthorize_user' in request.POST:
        id_profile = request.POST.get('id_profile')
        profile = Profile.objects.filter(pk=id_profile)
        if profile.count() != 0:
            profile = profile[0]
            profile.authorized = False
            profile.save()

    pending_users = Profile.objects.filter(authorized=False)
    authorized_users = Profile.objects.filter(authorized=True)

    template = get_template('admins/list_users.html')
    ctx = {
        'pending_users': pending_users,
        'authorized_users': authorized_users
    }

    return HttpResponse(template.render(ctx, request))
