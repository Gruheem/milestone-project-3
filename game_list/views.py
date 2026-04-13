from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import BoardGame
from review_comment.forms import ReviewForm

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

    approved_reviews = boardgame.reviews.filter(approved=True).order_by('-created_at')
    if request.user.is_authenticated:
        pending_reviews = boardgame.reviews.filter(approved=False,author=request.user)
    else:
        pending_reviews = boardgame.reviews.none()
    reviews = (approved_reviews | pending_reviews).distinct().order_by('-created_at')

    review_form = ReviewForm()

    # for review in reviews:
    #     review.approved_comments = review.comments.filter(approved=True)

    return render(
        request,
        "game_list/game_detail.html",
        {
            "boardgame": boardgame,
            "reviews": reviews,
            "review_form": review_form,
        }
    )