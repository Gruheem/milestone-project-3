from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import BoardGame

# Create your views here.
class GameList(generic.ListView):
    queryset = BoardGame.objects.filter(status=1)
    template_name = "index.html"
    paginate_by = 6

def game_detail(request, title):
    """
    Display an individual :model:`game_list.BoardGame`.

    **Context**

    ``boardgame``
        An instance of :model:`game_list.BoardGame`.

    **Template:**

    :template:`game_list/game_detail.html`
    """
    
    queryset = BoardGame.objects.filter(status=1)
    boardgame = get_object_or_404(queryset, title=title)
    reviews = boardgame.reviews.all().order_by('-created_at')

    return render(
        request,
        "game_list/game_detail.html",
        {
            "boardgame": boardgame, 
            "reviews": reviews,
        }
    )