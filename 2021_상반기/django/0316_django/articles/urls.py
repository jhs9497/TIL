from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # READ
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),

    # CREATE
    path('new/', views.new, name='new'),
    # DELETE
    
    # UPDATE
    path('<int:article_pk>/update/', views.update, name='update'),
]
