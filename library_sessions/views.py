from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from game_list.models import BoardGame
from .models import LibraryEntry, PlaySession
from .forms import PlaySessionForm

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


# Play Session Views
@login_required
def play_session_page(request, entry_id):
    entry = get_object_or_404(LibraryEntry, id=entry_id, user=request.user)
    boardgame = entry.boardgame

    # Get sessions where the user is host or tagged as a player
    sessions = PlaySession.objects.filter(boardgame=boardgame).filter(models.Q(host=request.user) | models.Q(players=request.user)).distinct().order_by('-date_played')

    if request.method == "POST":
        form = PlaySessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.approved = False
            session.host = request.user
            session.boardgame = boardgame
            session.save()
            form.save_m2m()
            messages.success(request, f'Play session logged for {boardgame.title}')
            return redirect('play_session_page', entry_id=entry_id)

    form = PlaySessionForm()

    return render(
        request,
        'library_sessions/play_session.html',
        {
            'entry': entry,
            'boardgame': boardgame,
            'sessions': sessions,
            'form': form,
        }
    )

@login_required
def edit_session(request, entry_id, pk):
    entry = get_object_or_404(LibraryEntry, id=entry_id, user=request.user)
    session = get_object_or_404(PlaySession, id=pk, boardgame=entry.boardgame)

    if request.method == "POST":
        form = PlaySessionForm(request.POST, instance=session)

        if form.is_valid():
            edited_session = form.save(commit=False)
            edited_session.approved = False
            edited_session.save()
            form.save_m2m()

            messages.success(request, "Session updated and awaiting approval.")
        else:
            messages.error(request, "Could not update session.")

    return redirect('play_session_page', entry_id=entry_id)

@login_required
def delete_session(request, entry_id, pk):
    session = get_object_or_404(PlaySession, id=pk, host=request.user)

    if request.method == "POST":
        session.delete()
        messages.success(request, "Play session deleted successfully.")

    return redirect('play_session_page', entry_id=entry_id)