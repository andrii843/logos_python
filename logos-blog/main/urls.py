from django.urls import path

from main.views import article_view
from main.views import main_view
from main.views import article_add

app_name = "main"

urlpatterns = [
    path(
        '',
        main_view,
        name='home'
    ),
    path(
        'article/<int:article_id>/',
        article_view,
        name='single-article'
    ),
    path(
        'article/add/',
        article_add,
        name='add-article'
    ),
]
