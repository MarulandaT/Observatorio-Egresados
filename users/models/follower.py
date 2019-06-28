from django.db import models

class Follower(models.Model):
    user = models.ForeignKey(
        'users.Profile',
        verbose_name='Seguidor',
        on_delete=models.CASCADE,
        related_name='follower_user'
    )
    account = models.ForeignKey(
        'users.Profile',
        verbose_name='Cuenta a seguir',
        on_delete=models.CASCADE,
        related_name='following_account'
    )

    def save(self, *args, **kwargs):
        if self.user != self.account:
            super(Follower, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Seguidor'
        verbose_name_plural = 'Seguidores'
