from django.contrib import admin
from users.models import Profile, Follower

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_filter = ('created', 'modified')

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'account',)
    list_filter = ('user', 'account',)
