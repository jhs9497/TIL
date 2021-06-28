from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-created_at')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def write(request):
    # 1. form에 담긴 정보를 꺼낸다.
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. 정보가 유효한지 검사한다 (오늘은 생략).

    # 3. 저장한다.
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:index')

    # context = {
    #     'article': article, # article 객체 (title, content 속성 보유)
    # }

    # return render(request, 'articles/write.html', context)
