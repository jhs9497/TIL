from django.urls import path
from . import views


urlpatterns = [
    path('signin', views.signup),

    # 유저정보 가져오기 by username
    path('auth/userinfo', views.userinfo),

    # 유저정보 다가져오기!
    path('alluserinfo/', views.alluserinfo),
]
