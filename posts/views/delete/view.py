from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def delete_post_view(request, id_post):
    from posts.models import Post, Like
    profile = request.user.profile

    if profile.type_user != 'admin' and profile.type_user != 'superadmin':
        return redirect('/posts/%i/' % id_post)

    post = Post.objects.filter(
        pk=id_post
    )
    if post.count() == 0:
        return redirect('/posts/%i/' % id_post)
    post = post[0]
    post.delete()

    return redirect('/')
