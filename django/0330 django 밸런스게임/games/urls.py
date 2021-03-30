from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/next/', views.next, name='next'),
    path('before/<int:pk>/', views.before, name='before'),
]
