from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # commit=False
            # 실제 DB에 저장은 하지 않지만
            # form에 담긴 인스턴스를 반환합니다.
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect(article)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # 게시글 작성자만 삭제 할 수 있도록
    if article.author == request.user:
        article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if article.author != request.user:
        return redirect('articles:index')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def create_comment(request, article_pk):
    if not request.user.id_athenticated:
        return redirect('accounts:login')

    # 1. 댓글이 가리킬 게시글을 가져옵니다.
    article = Article.objects.get(pk=article_pk)
    # 2. 사용자 입력값 (댓글)을 거내서
    form = CommentForm(request.POST)
    # 3. 유효성 검사를 하고
    if form.is_valid():
        # 4. 저장합니다.
        # save()
        # 1) 데이터베이스 인스턴스(객체)를 만든다.
        # 2) 인스턴스를 DB에 저장한다

        # commit=False 설정시 시점에 DB 저장 X
        # article 정보가 빠져있으므로 1)번만 실행하게 만드는것이 commit=False
        # PK값이 없는 comment를 반환
        comment = form.save(commit=False)
        comment.article = article
        comment.save() # 이 시점에 DB 반영
    return redirect('articles:detail', article.pk)
        

