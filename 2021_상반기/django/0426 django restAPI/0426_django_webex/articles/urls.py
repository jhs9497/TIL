from django.urls import path
from . import views

urlpatterns = [
    # 모든 게시글을 반환하는 URL
    # GET http://localhost:8000/api/v1/articles/
    # (동사) 행위는 HTTP method로 표현
    # (명사) 자원은 URL로 표현
    path('articles/', views.article_list),
]
