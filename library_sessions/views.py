from django.shortcuts import render
from .models import LibraryEntry

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