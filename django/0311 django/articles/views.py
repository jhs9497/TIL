from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    '''
    사용자에게 게시글 작성 Form을 반환합니다.
    '''
    return render(request, 'articles/new.html')


def write(request):
    '''
    게시글 정보를 받아서 저장합니다.
    '''
    # 1. form에 담긴 정보를 꺼낸다.
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 2. 유효성 검사를 실시한다.
    # 3. 저장 후 응답.
    article = Article(title=title, content=content)
    article.save()

    context = {
        'article': article,
    }
    return render(request, 'articles/write.html', context)
     
