"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views
from .views.like import like_post_view
from .views.delete import delete_post_view

urlpatterns = [
    path('',views.PostsFeedView.as_view()),
    path('posts/new/',views.CreatePostView.as_view()),
    path('posts/<int:pk>/',views.PostDetailView.as_view()),
    path('posts/like/<int:id_post>/', like_post_view),
    path('posts/unlike/<int:id_post>/', like_post_view),
    path('posts/delete/<int:id_post>/', delete_post_view),
]
