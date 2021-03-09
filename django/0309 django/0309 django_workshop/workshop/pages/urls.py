from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    #http://localhost:8000/dinner/

    #http://localhost:8000/dinner/저녁메뉴/인원수
    #.../dinner/샐러드/10/ 이런식으로 넘길수 있다
    path('<str:menu>/<int:people>/', views.dinner, name='dinner'),
]
