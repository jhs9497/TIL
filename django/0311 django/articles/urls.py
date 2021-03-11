from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # C - CREATE
    path('new/', views.new, name='new'),
    path('write/', views.write, name='write'),

    # R - READ
    path('', views.index, name='index'),

    # U - UPDATED

    # D - DELETE
]
