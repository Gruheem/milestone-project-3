from .models import Review, Comment
from django import forms


class ReviewForm(forms.ModelForm):
    """Form for creating and editing reviews."""
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')
        


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments on reviews."""
    class Meta:
        model = Comment
        fields = ('content',)
        