from django.shortcuts import render

# from django.http import HttpResponse

from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse

from main.models import Article
from tags.models import Tag
from comments.models import Comment


def article_view(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article)
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'main/single_article.html', context)


def main_view(request):
    articles = Article.objects.all()[:10]
    context = {
        'articles': articles,
    }
    return render(request, 'main/home.html', context)

def article_add(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        context = {
            'tags': tags
        }
        return render(request, 'main/add.html', context)
    elif request.user.is_authenticated and request.POST:
        # return HttpResponse(request)
        article = Article()
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.author = request.user
        article.image = request.FILES['image']
        article.save()

        return redirect(
            reverse('main:home')
        )
    else:
        return HttpResponseNotFound()