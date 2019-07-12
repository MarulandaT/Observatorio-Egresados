from django.contrib import admin
from users.models import Profile, Follower
from users.models.profile import Subject
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_filter = ('created', 'modified')

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'account',)
    list_filter = ('user', 'account',)

class InterestsAdmin(admin.ModelAdmin):
    display = ('name')


admin.site.register(Subject, InterestsAdmin)