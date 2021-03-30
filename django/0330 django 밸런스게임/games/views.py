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
    like = Like()
    like.number = game
    like.save()
    context = {
        'game': game,
        'like': like,
    }
    return render(request, 'games/detail.html', context)


def next(request, pk):
    pk = pk+1
    game = Game.objects.get(pk=pk)
    like = Like()
    like.number = game
    like.save()
    context = {
        'game': game,
        'like': like,
    }
    return render(request, 'games/detail.html', context)


def before(request, pk):
    pk = pk-1
    game = Game.objects.get(pk=pk)
    like = Like()
    like.number = game
    like.save()
    context = {
        'game': game,
        'like': like,
    }
    return render(request, 'games/detail.html', context)


def A_like_up(request, like_pk, game_pk):
    like = Like.objects.get(pk=like_pk)
    like.optionA = like.optionA + 1
    like.save()
    return redirect('games:detail', game_pk)


def B_like_up(request, like_pk, game_pk):
    like = Like.objects.get(pk=like_pk)
    like.optionB = like.optionB + 1
    like.save()
    redirect('games:detail', game_pk)





