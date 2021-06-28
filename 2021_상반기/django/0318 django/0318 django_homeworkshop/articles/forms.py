from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # title = forms.CharField()
    # content = forms.CharField()

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)