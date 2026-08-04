from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request, 'web/index.html', {
        "games": Game.objects.all(),
        "characters": Character.objects.all()
    })

def game(request, slug):
    game = Game.objects.get(slug=slug)
    return render(request, 'web/game.html', {
        "game": game
    })