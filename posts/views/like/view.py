from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def like_post_view(request, id_post):
    from posts.models import Post, Like
    profile = request.user.profile
    post = Post.objects.filter(
        pk=id_post
    )
    if post.count() == 0:
        return redirect('/posts/%i/' % id_post)
    post = post[0]

    if Like.objects.filter(post=post, user=profile).count() != 0:
        likes = Like.objects.filter(post=post, user=profile)
        likes.delete()
        return redirect('/posts/%i/' % id_post)

    new_like = Like(
        user=profile,
        post=post
    )
    new_like.save()

    return redirect('/posts/%i/' % id_post)
