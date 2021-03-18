from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # Form 할 때 주석 해제
    # path('new/', views.new, name='new'), 
    
    # modelForm 할 때 주석 해제
    # path('create/', views.create, name='create'), 
    # path('<int:pk>/update/', views.update, name='update'),
]
