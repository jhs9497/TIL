from django.shortcuts import render, redirect

# Create your views here.
def index(request, pk):
    games = Article.objects.get(pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'games/index.html', context)