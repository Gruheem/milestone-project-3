from django import forms
from .models import Genre, BoardGame

class GameFilterForm(forms.Form):
    """Form for filtering games by title and genre."""
    query = forms.CharField(required=False, label='Search Title:')
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label='Genre:',
        empty_label='All Genres'
    )


class BoardGameForm(forms.ModelForm):
    """Form for creating and editing board game entries."""
    # Allow multiple genres to be selected using checkboxes
    genre_id = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Genre(s)'
    )

    class Meta:
        model = BoardGame
        fields = ['title', 'description', 'min_players', 'max_players', 'min_age', 'play_time', 'complexity', 'genre_id', 'publisher', 'year_published', 'image']
        labels = {
            'title': 'Game Title',
            'description': 'Description',
            'min_players': 'Minimum Players',
            'max_players': 'Maximum Players',
            'min_age': 'Minimum Age',
            'play_time': 'Play Time (minutes)',
            'complexity': 'Complexity (1-10)',
            'publisher': 'Publisher',
            'year_published': 'Year Published',
            'image': 'Game Image (optional)',
        }
        widgets = {
            'min_age': forms.NumberInput(attrs={'min': 0}),
            'complexity': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'year_published': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }