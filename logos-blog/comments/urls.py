from django.urls import path

from comments.views import add_comment
from comments.views import get_comments

app_name = "comments"

urlpatterns = [
    path(
        'add',
        add_comment,
        name='add_comment',
    ),
    path(
        'get',
        get_comments,
        name='get_comments',
    ),
]
