"""Users URLs."""

# Django
from django.urls import path

# View
from users import views
from django.urls import include, path, re_path
from .views.admins.list import view as list_users_view
from .views.superuser.list import view as list_admins_view
from django.contrib.auth.views import LoginView, password_reset, password_reset_done , password_reset_confirm, password_reset_complete

urlpatterns = [

    # Management
    path('login/',view=views.login_view),
    path('logout/',view=views.logout_view),
    path('signup/',view=views.SignupView.as_view()),
    re_path(r'^password_reset/$', password_reset,{'email_template_name':'users/password_reset_email.html',
                                                    'template_name':'users/password_reset_form.html',
                                                    'post_reset_redirect':'/users/password_reset/done/',
                                            
                                                    },name='password_reset'),

    re_path(r'^password_reset/done/$',password_reset_done, {'template_name': 'users/password_reset_done.html'}, name='password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
                                                    {'template_name': 'users/password_reset_confirm.html',
                                                    'post_reset_redirect': '/users/reset/done/'},
                                                    name='password_reset_confirm'),

    re_path(r'^reset/done/$', password_reset_complete, {'template_name': 'users/password_reset_complete.html'},name='password_reset_complete'),
    path('me/profile/',view=views.UpdateProfileView.as_view()),

    # Posts
    path('<str:username>/',view=views.UserDetailView.as_view()),
    path('admins/list/', list_users_view),
    path('superuser/list/', list_admins_view)
]
