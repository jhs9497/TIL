from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # C - CREATE
    path('new/', views.new, name='new'),
    path('write/', views.write, name='write'),

    # R - READ
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),

    # U - UPDATED
    # 사용자 입장에서의 수정 로직
    # 1. 게시글 수정 버튼을 누른다.
    # 2. 게시글을 수정한다.
    # 3. 게시글 수정 완료 버튼을 누른다.
    # 4. 수정된 게시글을 본다.

    # 개발자 입장에서의 수정 로직
    # 1. 수정 버튼을 만든다 (UI).
    # 2. 원래 글의 내용이 담긴 수정 페이지를 보여준다.
    # 3. 수정된 내용을 받아서, 기존의 게시글을 업데이트한다.
    # 4. 업데이트 후 업데이트된 내용을 사용자에게 보여준다.
    path('<int:article_id>/edit/', views.edit, name='edit'),
    path('<int:article_id>/update/', views.update, name='update'),

    # D - DELETE
    path('<int:article_id>/delete/', views.delete, name='delete'),
]
