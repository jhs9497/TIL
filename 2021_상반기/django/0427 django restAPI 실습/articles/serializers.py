from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    '''
    articles 전용
    모델을 어떻게 직렬화할 것인지 설정하는 것이 포인트
    '''
    class Meta:
        model = Article
        fields = ['id', 'title', 'content',]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content', 'article']
        read_only_fields = ['article']


class ArticleSerializer(serializers.ModelSerializer):
    '''
    개별 article 전용
    모델을 어떻게 직렬화할 것인지 설정하는 것이 포인트
    '''

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'comment_set', 'comment_count']



