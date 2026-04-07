from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class BoardGame(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year_published = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    min_age = models.IntegerField()
    play_time = models.IntegerField()
    complexity = models.IntegerField()
    description = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='board_games')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_games')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.title} | added by {self.added_by.username}'

