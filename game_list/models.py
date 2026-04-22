from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    # class Meta:
    #     ordering = ['title']

    def __str__(self):
        return f'{self.name}'

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
    genre_id = models.ManyToManyField(Genre, related_name='games')
    image = CloudinaryField('image', default='placeholder')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_games')
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} | added by {self.added_by.username}'

