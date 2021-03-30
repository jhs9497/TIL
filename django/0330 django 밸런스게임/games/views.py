from django.shortcuts import render, redirect
from .models import Game, Like

# Create your views here.
def index(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'games/index.html', context)


def detail(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game
    }
    return render(request, 'games/detail.html', context)


def next(request, pk):
    pk = pk+1
    game = Game.objects.get(pk=pk)
    context = {
        'game': game
    }
    return render(request, 'games/detail.html', context)


def before(request, pk):
    pk = pk-1
    game = Game.objects.get(pk=pk)
    context = {
        'game': game
    }
    return render(request, 'games/detail.html', context)

