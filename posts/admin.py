"""Posts model."""

# Django
from django.contrib import admin

# Models
from posts.models import Post, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'photo')
    list_filter = ('created', 'modified')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user',)
    list_filter = ('post', 'user',)
