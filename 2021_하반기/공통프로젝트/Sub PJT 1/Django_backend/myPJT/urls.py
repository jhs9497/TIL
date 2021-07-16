"""myPJT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 로그인 기능
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    # User관리
    path('accounts/', include('accounts.urls')),
    # Movie 정보 api
    path('api/v1/', include('movies.urls')),

    # 로그인 기능
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
