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

    def __str__(self):
        return f'{self.user.username} - {self.boardgame.title} ({self.status})'

class PlaySession(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_sessions')
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name='play_sessions')
    date_played = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)
    players = models.ManyToManyField(User, related_name='play_sessions', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.boardgame.title} logged by {self.host.username} on {self.date_played}'
    

