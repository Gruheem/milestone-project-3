from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
from review_comment import models
from .forms import BoardGameForm, GameFilterForm
from review_comment.models import Comment, Review
from .models import BoardGame
from review_comment.forms import ReviewForm, CommentForm
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
class GameList(generic.ListView):
    template_name = "game_list/index.html"
    paginate_by = 12

    # Creates list of games and Handles the search filters.
    def get_queryset(self):
        approved = BoardGame.objects.filter(approved=True)
        if self.request.user.is_authenticated:
            pending = BoardGame.objects.filter(approved=False, added_by=self.request.user)
        else:
            pending = BoardGame.objects.none()

        queryset = (approved | pending).distinct().order_by('-created_at')

        self.form = GameFilterForm(self.request.GET)

        if self.form.is_valid():    
            query = self.form.cleaned_data.get('query')
            genre = self.form.cleaned_data.get('genre')

            if query:
                queryset = queryset.filter(title__icontains=query)
            if genre:
                queryset = queryset.filter(genre_id=genre)

        # returns set of BoardGame objects with extra 'field' avg_rating.
        return queryset.annotate(avg_rating=Avg('reviews__rating'))
    
    # Gets and Extends the context data of our Generic ListView to include the form in the template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form

        return context

# Add a Game Page
@login_required
def add_game(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.status = 0
            game.added_by = request.user
            game.save()
            form.save_m2m()
            messages.success(request, 'Game added and awaiting approval')
            return redirect('home')
    
    else:
        form = BoardGameForm()

    return render(
        request, 
        'game_list/add_game.html', 
        {'form': form},
        )

# Edit a Game Page
@login_required
def edit_game(request, game_id):
    boardgame = get_object_or_404(BoardGame, id=game_id, added_by=request.user)

    if request.method == "POST":
        form = BoardGameForm(request.POST, instance=boardgame)
        if form.is_valid():
            edited_game = form.save(commit=False)
            edited_game.approved = False
            edited_game.save()
            form.save_m2m()
            messages.success(request, f'{boardgame.title} updated and awaiting re-approval')
            return redirect('home')
    else:
        form = BoardGameForm(instance=boardgame)

    return render(
        request, 
        'game_list/edit_game.html', 
        {
            'form': form, 
            'boardgame': boardgame
            }
    )


# Game Detail Page
def game_detail(request, slug):
    """
    Display an individual :model:`game_list.BoardGame`.

    **Context**

    ``boardgame``
        An instance of :model:`game_list.BoardGame`.

    **Template:**

    :template:`game_list/game_detail.html`
    """ 
    # Crashes if trying to use Q method when not logged in
    if request.user.is_authenticated:
        queryset = BoardGame.objects.filter(Q(approved=True) | Q(added_by=request.user), slug=slug)
    else:
        queryset = BoardGame.objects.filter(approved=True, slug=slug)

    boardgame = get_object_or_404(queryset)

    avg_rating = boardgame.reviews.filter(approved=True).aggregate(Avg('rating'))['rating__avg']

    # Get approved reviews and pending reviews for the current user, then combine them and order by creation date.
    approved_reviews = boardgame.reviews.filter(approved=True).order_by('-created_at')
    if request.user.is_authenticated:
        pending_reviews = boardgame.reviews.filter(approved=False,author=request.user)
    else:
        pending_reviews = boardgame.reviews.none()
    reviews = (approved_reviews | pending_reviews).distinct().order_by('-created_at')

    # Handles the submission of both forms, uses if/elif to determine which form was submitted as there are two on one page.
    if request.method == "POST":
        # Create Review
        if "review_submit" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review.boardgame = boardgame
                review.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Review submitted and awaiting approval'
                )
                return redirect('game_detail', slug=boardgame.slug)
        # Create Comment
        elif "comment_submit" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.review_id = request.POST.get("review_id")
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
                )
                return redirect('game_detail', slug=boardgame.slug)

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
            "avg_rating": avg_rating,
        }
    )

# Edit Review
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            edited_review = form.save(commit=False)
            edited_review.approved = False
            edited_review.save()
            messages.success(request, 'Review updated and awaiting approval')
    else:
        messages.error(request, 'Invalid request')

    return redirect('game_detail', slug=review.boardgame.slug)

# Delete Review
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == "POST":
        game_slug = review.boardgame.slug
        review.delete()
        messages.success(request, 'Review deleted')
        return redirect('game_detail', slug=game_slug)

    return redirect('game_detail', slug=review.boardgame.slug)

# Edit Comment
@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            edited_comment = form.save(commit=False)
            edited_comment.approved = False
            edited_comment.save()
            messages.success(request, 'Comment updated and awaiting approval')
    else:
        messages.error(request, 'Invalid request')

    return redirect('game_detail', slug=comment.review.boardgame.slug)

# Delete Comment
@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == "POST":
        game_slug = comment.review.boardgame.slug
        comment.delete()
        messages.success(request, 'Comment deleted')
        return redirect('game_detail', slug=game_slug)

    return redirect('game_detail', slug=comment.review.boardgame.slug)

# Custom 404 Pages
def custom_404(request, exception):
    if request.user.is_authenticated:
        return render(request, '404_user.html', status=404)
    else:
        return render(request, '404_guest.html', status=404)