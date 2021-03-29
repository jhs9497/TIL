from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            articles = form.save()
            return redirect('articles:detail', articles.pk)
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # articles = Article(title=title, content=content)
    # articles.save()
    form = ArticleForm
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles':articles
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    articles = Article.objects.get(pk=pk)
    articles.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article':article
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
        context = {
            'form':form,
            'article':article
        }
        return render(request, 'articles/update.html', context)

