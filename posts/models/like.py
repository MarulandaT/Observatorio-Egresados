from django.db import models

class Like(models.Model):
    user = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        verbose_name='Usuario',
        related_name='user_liked'
    )
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        verbose_name='Post',
        related_name='post_liked'
    )

    class Meta:
        verbose_name = 'Like'

    def __str__(self):
        return 'Like de %s a publicación %i' % (self.user, self.post.pk)
