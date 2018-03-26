from django.urls import path

from main.views import article_view
from main.views import main_view
from main.views import add_article_view
from main.views import like_article

app_name = "main"

urlpatterns = [
    path(
        '',
        main_view,
        name='home'
    ),
    path(
        '<int:article_id>/',
        article_view,
        name='single-article'
    ),
    path(
        'add-article/',
        add_article_view,
        name='add-article',
    ),
    path(
        'like-article',
        like_article,
        name='like-article',
    )
]
