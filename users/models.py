from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    AUTHOR = 'author'
    USER = 'user'
    USER_ROLES = [
        (ADMIN, 'Admin role'),
        (USER, 'User role'),
        (AUTHOR, 'Author role'),
    ]

    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default='user',
    )

    class Meta:
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_author(self):
        return self.role == self.AUTHOR

    def __str__(self):
        return self.username
