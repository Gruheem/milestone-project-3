from django.shortcuts import render
from django.views import generic
from .models import BoardGame

# Create your views here.
class GameList(generic.ListView):
    queryset = BoardGame.objects.filter(status=1)
    template_name = 'boardgame_list.html'