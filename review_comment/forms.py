from .models import Review, Comment
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }