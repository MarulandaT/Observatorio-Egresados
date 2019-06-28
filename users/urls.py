"""Users URLs."""

# Django
from django.urls import path

# View
from users import views
from .views.admins.list import view as list_users_view
from .views.superuser.list import view as list_admins_view

urlpatterns = [

    # Management
    path('login/',view=views.login_view),
    path('logout/',view=views.logout_view),
    path('signup/',view=views.SignupView.as_view()),
    path('me/profile/',view=views.UpdateProfileView.as_view()),

    # Posts
    path('<str:username>/',view=views.UserDetailView.as_view()),
    path('admins/list/', list_users_view),
    path('superuser/list/', list_admins_view)
]
