
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render

from comments.models import Comment


def add_comment(request, article_id):
    if request.user.is_authenticated and request.POST:
        comment = Comment()
        comment.author = request.user
        comment.article_id = article_id
        comment.content = request.POST["comment_body"]
        comment.save()
        return redirect(
            reverse('main:single-article', args=[article_id])
        )
    else:
        return HttpResponseNotFound()
