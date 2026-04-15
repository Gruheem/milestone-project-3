from django.shortcuts import render
from game_list.models import BoardGame
from .models import LibraryEntry
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
def library_page(request):
    """
    Display the user's library of board games.

    **Context**

    ``library_entries``
        A queryset of :model:`library_sessions.LibraryEntry` instances for the current user.

    **Template:**

    :template:`library_sessions/library.html`
    """ 
    entries = LibraryEntry.objects.filter(user=request.user).order_by('-added_at')
    return render(
        request, 
        'library_sessions/library.html', 
        {'entries': entries}
    )

@login_required
def remove_from_library(request, entry_id):
    entry = get_object_or_404(LibraryEntry, id=entry_id, user=request.user)
    if request.method == "POST":
        game_title = entry.boardgame.title
        entry.delete()
        messages.success(request, f'{game_title} removed from your library')
        return redirect('library_page')
    return redirect('library_page')

@login_required
def add_to_library(request, boardgame_id):
    game = get_object_or_404(BoardGame, id=boardgame_id)
    if request.method == "POST":
        status = request.POST.get('status')
        entry, created = LibraryEntry.objects.get_or_create(
            user=request.user,
            boardgame=game,
            defaults={'status': status}
        )
        if created:
            messages.success(request, f'{game.title} added to your library')
        else:
            messages.info(request, f'{game.title} is already in your library')
    return redirect('game_detail', title=game.title)