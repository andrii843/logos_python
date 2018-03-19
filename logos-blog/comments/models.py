from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):

    content = models.TextField(
        verbose_name='Comment content'
    )
    article = models.ForeignKey(
        'main.Article',
        on_delete=models.CASCADE,
        verbose_name='Article'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return '{}...'.format(self.content[:10])
