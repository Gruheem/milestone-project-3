from django import forms
from .models import Genre, BoardGame
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class GameFilterForm(forms.Form):
    query = forms.CharField(required=False, label='Search Title:')
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label='Genre:',
        empty_label='All Genres'
    )


class BoardGameForm(forms.ModelForm):
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
            'complexity': 'Complexity (1-5)',
            'publisher': 'Publisher',
            'year_published': 'Year Published',
            'image': 'Game Image (optional)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'min_age': forms.NumberInput(attrs={'min': 0}),
            'complexity': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'year_published': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }

    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
        
    #     self.helper.layout = Layout(
    #         'title',
    #         'description',
    #         'min_players',
    #         'max_players',
    #         'min_age',
    #         'play_time',
    #         'complexity',
    #         Field('genre_id', wrapper_class='genre-columns'),
    #         'publisher',
    #         'year_published',
    #     )