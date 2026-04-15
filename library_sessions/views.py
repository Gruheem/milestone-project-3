from django.shortcuts import render
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