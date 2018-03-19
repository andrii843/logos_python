from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from tags.models import Tag


class Article(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created'
    )
    image = models.ImageField(
        upload_to='articles_images',
        verbose_name='Image',
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    content = models.TextField(
        verbose_name='Content'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Tags',
        help_text='Tags for dividing articles to categories',
    )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:single-article', args=[self.id])
