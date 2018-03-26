from django.http import HttpResponseNotFound
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse

from comments.models import Comment
from comments.forms import CommentForm

from django.template.loader import render_to_string
from django.http import JsonResponse

def add_comment(request):
    if request.user.is_authenticated and request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                author=request.user,
                article_id=form.cleaned_data["article_id"],
                content=form.cleaned_data["content"],
            )
            return redirect(
                reverse('main:single-article', args=[comment.article_id])
            )
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()

def get_comments(request):
    if request.user.is_authenticated and request.is_ajax():
        article_id = request.GET['article_id']
        num = int(request.GET['num'])
        
        comments = Comment.objects.filter(article_id=article_id).order_by('-id')[num*2:num*2+2]
        rendered = render_to_string('comments/comments.html', {'comments': comments})

        return JsonResponse({'content': rendered})
    else:
        return HttpResponseBadRequest()