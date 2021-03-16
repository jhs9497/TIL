from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 1. DB에서 게시글 전부 가져옵니다.
    article_list = Article.objects.all()

    # 2. context에 담아서 index.html로 넘겨줍니다.
    context = {
        'article_list': article_list,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context ={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    if request.method == 'POST':
        # 폼 인스턴스를 생성하고 요청에 의한 데이터로 채웁니다. (binding)
        form = ArticleForm(request.POST)
        # 폼에 바인딩된 데이터가 유효한지 검사합니다.
        # is_valid() 메서드는 True/False를 반환합니다.
        if form.is_valid():
            # form.cleaned_data에서 검증된 데이터를 꺼냅니다.
            # cleaned_data는 유효성 검사를 통과한 데이터가 담긴 딕셔너리.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # Article.objects.create(title=title, content=content)
            # 위의 3줄은
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm() # request.method가 get요청이면 빈 form이 담기게 된다

    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context) # 빈 form일시 context는 빈 값으로 그냥 new.html보여준다


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # 새로 작성된 게시글 정보를 꺼냅니다.
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        
        # 기존 게시글의 내용에 덮어 씌웁니다.
        # article.title = title
        # article.content = content
        # article.save()
        form = ArticleForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('articles:index') 

    else:
        form = ArticleForm(instance=article)
    # 기존의 내용을 가져와서 넘겨준다.
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)


