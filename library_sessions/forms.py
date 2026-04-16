from django import forms
from .models import PlaySession

class PlaySessionForm(forms.ModelForm):
    class Meta:
        model = PlaySession
        fields = ['boardgame', 'date_played', 'duration', 'notes', 'players']
        # Styling for the form fields
        widgets = {
            'date_played': forms.DateInput(attrs={'type': 'date'}),
            'duration': forms.NumberInput(attrs={'placeholder': 'Duration in minutes'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'How did it go?'}),
        }
        labels = {
            'date_played': 'Date Played',
            'duration': 'Duration (minutes)',
            'notes': 'Notes (optional)',
            'players': 'Tag Players',
        }