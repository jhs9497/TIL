from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/next/', views.next, name='next'),
    path('before/<int:pk>/', views.before, name='before'),
    path('<int:like_pk>/<int:game_pk>/A_like_up/', views.A_like_up, name='A_like_up'),
    path('<int:like_pk>/<int:game_pk>/B_like_up/', views.B_like_up, name='B_like_up'),
] 
