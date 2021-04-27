from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    '''
    articles 전용
    모델을 어떻게 직렬화할 것인지 설정하는 것이 포인트
    '''
    class Meta:
        model = Article
        fields = ['id', 'title', 'content',]


class ArticleSerializer(serializers.ModelSerializer):
    '''
    개별 article 전용
    모델을 어떻게 직렬화할 것인지 설정하는 것이 포인트
    '''
    class Meta:
        model = Article
        fields = ['id', 'title',]

