from main.models import Article
from comments.models import Comment


def sidebar(request):
    articles = Article.objects.all().order_by('-created')[:3]
    latest_comments = Comment.objects.all()[:5]
    print(articles)
    return {
        'latest_articles': articles,
        'latest_comments': latest_comments,
    }
