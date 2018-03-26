from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.http import HttpResponse

from main.models import Article
from main.models import ArticleLike
from main.forms import ArticleForm

from comments.models import Comment
from comments.forms import CommentForm

def article_view(request, article_id, comment_form=None):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article).order_by('-id')[:2]
    article.liked = article.likes.filter(user=request.user).exists()

    context = {
        'article': article,
        'comments': comments,
        'add_comment_form': CommentForm(initial={
            'article_id': article_id,
        })
    }
    return render(request, 'main/single_article.html', context)


def main_view(request):
    articles = Article.objects.all()[:10]
    context = {
        'articles': articles,
    }
    return render(request, 'main/home.html', context)


def add_article_view(request):
    if request.method == "GET":
        form = ArticleForm()
        context = {
            'add_article_form': form,
        }
        return render(request, 'main/add_article.html', context)
    else:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect(article.get_absolute_url())
        else:
            context = {
                'add_article_form': form,
            }
            return render(request, 'main/add_article.html', context)


def like_article(request):
    if request.user.is_authenticated and request.POST and request.is_ajax():
        print(request)
        article_id = request.POST['article_id']
        print(article_id)

        article = Article.objects.get(id=article_id)
        is_liked = article.likes.filter(user=request.user).exists()
        if is_liked:
            return HttpResponseBadRequest()

        new_like = ArticleLike.objects.create(
            user=request.user,
        )
        article.likes.add(new_like)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
