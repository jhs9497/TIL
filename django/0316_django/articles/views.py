from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 1. DB에서 게시글 전부 가져옵니다.
    article_list = Article.objects.all()

    # 2. context에 담아서 index.html로 넘겨줍니다.
    context = {
        'article_list': article_list,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    if request.method == 'POST':
        # 1. Form에서 넘어온 데이터를 꺼냅니다.
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 2. DB에 저장합니다.
        article = Article.objects.create(title=title, content=content)
        return redirect('articles:index')
    else:
        return render(request, 'articles/new.html')


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # 새로 작성된 게시글 정보를 꺼냅니다.
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 기존 게시글의 내용에 덮어 씌웁니다.
        article.title = title
        article.content = content
        article.save()

    else:
        # 기존의 내용을 가져와서 넘겨준다.
        context = {
            'article': article,
        }
        return render(request, 'articles/update.html', context)


