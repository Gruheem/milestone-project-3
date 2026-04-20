from django import forms
from .models import Genre, BoardGame


class GameFilterForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label='Genre',
        empty_label='All Genres'
    )


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['title', 'description', 'min_players', 'max_players', 'min_age', 'play_time', 'complexity', 'genre_id', 'publisher', 'year_published']
        labels = {
            'title': 'Game Title',
            'description': 'Description',
            'min_players': 'Minimum Players',
            'max_players': 'Maximum Players',
            'min_age': 'Minimum Age',
            'play_time': 'Play Time (minutes)',
            'complexity': 'Complexity (1-5)',
            'genre_id': 'Genre',
            'publisher': 'Publisher',
            'year_published': 'Year Published',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'min_age': forms.NumberInput(attrs={'min': 0}),
            'complexity': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'year_published': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }