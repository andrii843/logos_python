from django import forms

from main.models import Article


class ArticleForm(forms.ModelForm):

    # tags = 

    class Meta:
        model = Article
        exclude = ('author', 'created', )
