from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.http import HttpResponse, HttpResponseForbidden
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # hashtag 따로 저장
            for word in article.content.split():
                # word: ex) 오늘 장고는 #많이 # 힘들다
                if word.startswith('#'):
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                # hashtag 따로 저장
                # update에서는 hasgtag 관계를 초기화해줘야함
                article.hashtags.clear()
                for word in article.content.split():
                    # word: ex) 오늘 장고는 #많이 # 힘들다
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
        # return HttpResponseForbidden()
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
        

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')
    # return HttpResponse(status=401)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        # return HttpResponseForbidden()
    return redirect('articles:detail', article_pk)
    # return HttpResponse(status=401)


def like(request, pk):
    # 1. 좋아요 누른 게시글 가져오기
    article = get_object_or_404(Article, pk=pk)

    # 2. 게시글 좋아요 누른 유저목록에
    if article.like_users.filter(pk=request.user.pk).exists():
    # 내가 있다면 제거하기
        article.like_users.remove(request.user)
    else:
    # 내가 없다면 추가하기
        article.like_users.add(request.user)

    # print(article.like_users.all())
    # print(type(article.like_users))
    # print( help(article.like_users) )
    
    # 중계테이블을 통째로 가져오기
    # print(article.like_users.through.objects.all())
    
    return redirect('articles:detail', article.pk)


def hashtag(request, hash_pk):
    tag = get_object_or_404(Hashtag, pk=hash_pk)
    context = {
        'tag': tag
    }
    return render(request, 'articles/hashtag.html', context)
