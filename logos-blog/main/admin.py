from django.contrib import admin

from main.models import Article
from main.models import ArticleLike


admin.site.register(Article)
admin.site.register(ArticleLike)
