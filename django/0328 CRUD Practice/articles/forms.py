from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 100,
            }
        )
    )
    
    class Meta:
        model = Article
        fields = '__all__'