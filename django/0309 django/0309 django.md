#### MTV (일반적으론 MVC라 부름) 꼭 기억

> Model -> Template -> View

- http://localhost:8000/ == 루트 경로
- => 1. /pages/ - 루트 경로부터 시작
- =>  2. pages/ - 현재 위치부터 시작
- ex) 현재 위치가 https://localhost:8000/articles/ 라면
- pages/라고 쓰는 순간 https://localhost:8000/articles/pages/로 인식함 이상한 주소로 감

1. django-admin startproject config .

2. ls -> manage.py 있는지 확인  >config  manage.py<

3. python manage.py startapp pages

4. config-settings-installed_apps에서 'articles', 'pages', 추가

5. config-urls.py에

   from django.contrib import admin
   from django.urls import path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
       path('pages/', include('pages.urls')),

   ]

6. articles-urls.py생성하고

   from django.urls import path

   urlpatterns = [
       #http://localhost:8000/articles/
       path('', views.index),
   ]

7. articles-views.py

   from django.shortcuts import rende

   def index(request):

     return render(request, 'index.html')

8. articles-templates폴더생성-index.html생성

9. pages-urls.py생성하고

   from django.urls import path

   from . import views

   urlpatterns = [
       #http://localhost:8000/pages/
       path('', views.index),
   ]

10. pages-views.py

    from django.shortcuts import render

    def index(request):

      return render(request, 'index.html')

11. pages-templates폴더생성-index.html생성





