from django.db import models
from game_list.models import BoardGame
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    """Review of a board game with rating and approval status."""
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """Return review summary with author and game."""
        return f'Review by {self.author} on {self.boardgame}'

class Comment(models.Model):
    """Comment on a review awaiting approval."""
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """Return comment summary with author and review."""
        return f'Comment by {self.author} on {self.review}'