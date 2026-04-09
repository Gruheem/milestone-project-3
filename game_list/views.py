from django.shortcuts import render
from django.views import generic
from .models import BoardGame

# Create your views here.
class GameList(generic.ListView):
    queryset = BoardGame.objects.all()
    template_name = 'boardgame_list.html'