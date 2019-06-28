from django import template

register = template.Library()

@register.simple_tag
def is_liked_post(post, profile):
    from posts.models import Like

    return 'black' if Like.objects.filter(post=post, user=profile).count() == 0 else 'red'
