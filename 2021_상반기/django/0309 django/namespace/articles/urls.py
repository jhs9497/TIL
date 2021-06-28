from django.urls import path
from . import views

app_name = 'articles'  # url name을 구분해 주기 위한 prefix
urlpatterns = [
    #http://localhost:8000/articles/
    path('', views.index, name='index'),
]
