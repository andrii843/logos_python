from django.urls import path

from comments.views import add_comment


app_name = "comments"

urlpatterns = [
    path(
        'comment/<int:article_id>/',
        add_comment,
        name='add_comment',
    ),
]
