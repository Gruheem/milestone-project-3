from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import BoardGame
from review_comment.forms import ReviewForm, CommentForm
from django.shortcuts import redirect

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

    # Get approved reviews and pending reviews for the current user, then combine them and order by creation date.
    approved_reviews = boardgame.reviews.filter(approved=True).order_by('-created_at')
    if request.user.is_authenticated:
        pending_reviews = boardgame.reviews.filter(approved=False,author=request.user)
    else:
        pending_reviews = boardgame.reviews.none()
    reviews = (approved_reviews | pending_reviews).distinct().order_by('-created_at')

    # Handles the submission of both forms, uses if/elif to determine which form was submitted as there are two on one page.
    if request.method == "POST":

        if "review_submit" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review.boardgame = boardgame
                review.save()
                return redirect('game_detail', title=title)

        elif "comment_submit" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.review_id = request.POST.get("review_id")
                comment.save()
                return redirect('game_detail', title=title)

    review_form = ReviewForm()
    comment_form = CommentForm()

    return render(
        request,
        "game_list/game_detail.html",
        # Context
        {
            "boardgame": boardgame,
            "reviews": reviews,
            "review_form": review_form,
            "comment_form": comment_form,
        }
    )