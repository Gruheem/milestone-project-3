from django import forms
from .models import PlaySession

class PlaySessionForm(forms.ModelForm):
    class Meta:
        model = PlaySession
        fields = ['boardgame', 'date_played', 'duration', 'notes', 'players']
        