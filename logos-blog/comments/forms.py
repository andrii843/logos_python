from django import forms


class CommentForm(forms.Form):

    content = forms.CharField(
        label="Comment message",
        widget=forms.Textarea(),
    )
    article_id = forms.CharField(
        widget=forms.HiddenInput(),
    )
