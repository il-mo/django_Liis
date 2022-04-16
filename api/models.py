from django.db import models

from django_Liis import settings


class Post(models.Model):
    VISIBLE_CHOICES = [
        ('for_all', 'Пост виден всем'),
        ('for_followers', 'Пост виден только подписчикам'),
    ]
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    name = models.CharField(max_length=200, verbose_name='Название поста')
    text = models.TextField(verbose_name='Содержание')
    visible = models.CharField(
        max_length=25,
        verbose_name='Видимость поста',
        choices=VISIBLE_CHOICES,
        default='for_all',
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.name
