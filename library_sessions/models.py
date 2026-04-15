from django.db import models
from django.contrib.auth.models import User
from game_list.models import BoardGame

# Create your models here.
class LibraryEntry(models.Model):

    STATUS_CHOICES=[
        ('owned', 'Owned'), 
        ('wishlist', 'Wishlist')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure a user can only have one entry per board game (Safety at DB Level)
        unique_together = ('user', 'boardgame')