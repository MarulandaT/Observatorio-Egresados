"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

TYPE_USERS = [
    ('egresado', 'egresado'),
    ('admin', 'admin'),
    ('superadmin', 'superadmin')
]

class Subject(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    UNDEFINED = 'indef'
    MALE = 'masc'
    FEMALE = 'fem'
    GENDER_CHOICE = [
        (UNDEFINED, 'Indefinido'),
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(
        max_length=100,
        verbose_name='Tipo de usuario',
        choices=TYPE_USERS,
        default=TYPE_USERS[0][0]
    )
    authorized = models.BooleanField(
        default=False,
        verbose_name='Acceso autorizado'
    )

    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    city = models.TextField(max_length=20)
    dni_administrador = models.CharField(max_length=20)
    age = models.CharField(max_length=2, default=0)
    gender = models.CharField(max_length=4, choices=GENDER_CHOICE, default=UNDEFINED)
    confirmation_handling_sensitive_data = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    interests = models.ManyToManyField(Subject, related_name='interested_students')


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        """Return username."""
        return self.user.username

    def followers(self):
        from users.models import Follower
        return Follower.objects.filter(account=self).count()

    def following(self):
        from users.models import Follower
        return Follower.objects.filter(user=self).count()



