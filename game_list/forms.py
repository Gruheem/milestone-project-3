from django import forms
from .models import Genre


class GameFilterForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label='Genre',
        empty_label='All Genres'
    )