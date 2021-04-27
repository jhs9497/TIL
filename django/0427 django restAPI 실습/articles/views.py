from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404

from .models import Article, Comment
from .serializers import (
    ArticleSerializer, 
    ArticleListSerializer,
    CommentSerializer,
)

# Create your views here.
@swagger_auto_schema(methods=['POST'], request_body=ArticleListSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method =='GET':
        # HttpRequest (Django 내부적으로 사용하는 객체)
        # HttpRequest + a => api_view
        # 1. 모든게시글을 가져오고
        articles = Article.objects.all()

        # QuerySet => Python 기본 타입으로 바꿔줘야함
        # 이걸 해주는 DRF Serializers
        # 2. 직렬화 (시리얼라이즈)
        serializer = ArticleListSerializer(articles, many=True)
                            # 넘기는 데이터가 2개이상이면 many=True반드시!

        # 3. 직렬화된 데이터를 응답
        # Python 기본 타입 => JSON으로 변환
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data) # 바인딩
        if serializer.is_valid(raise_exception=True): 
            # 유효성검사 raise_exception은 유효성 검사 통과못했을 때 자동으로 400에러 뜨게 만들어줌
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED) # 응답

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method =='GET':
        serializer = ArticleSerializer(article) # 단일객체이므로 many=True 필요없음
        return Response(data=serializer.data)
    
    elif request.method == 'DELETE':
        article = article.delete()
        data = {
            'message': f'{article}이 삭제되었습니다.'
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)


@api_view()
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(data=serializer.data)


@api_view(['POST'])
def create_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(data=serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_id):
    '''
    http://localhost:8000/api/v1/commnets/<int:comment_id>/
    '''
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method =='GET':
        serializer = CommentSerializer(comment) # 단일객체이므로 many=True 필요없음
        return Response(data=serializer.data)
    
    elif request.method == 'DELETE':
        comment = comment.delete()
        data = {
            'message': f'{comment}이 삭제되었습니다.'
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

