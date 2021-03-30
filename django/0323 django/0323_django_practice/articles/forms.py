from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',)
        # __all__ 은 좋지 않은 습관!
        # exclude = ('title',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('__all__')
        
        
        # ('content',)
        


