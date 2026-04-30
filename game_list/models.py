from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_summernote.fields import SummernoteTextField
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Genre(models.Model):
    """Board game genre category."""
    name = models.CharField(max_length=100)

    # class Meta:
    #     ordering = ['title']

    def __str__(self):
        """Return the genre name."""
        return f'{self.name}'

class BoardGame(models.Model):
    """Board game entry with details and metadata."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True,)
    publisher = models.CharField(max_length=200)
    year_published = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    min_age = models.IntegerField()
    play_time = models.IntegerField()
    complexity = models.IntegerField()
    description = SummernoteTextField()
    genre_id = models.ManyToManyField(Genre, related_name='games')
    image = CloudinaryField('image', blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_games')
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """Generate slug from title if not provided, then save."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """Return title and contributor username."""
        return f'{self.title} | added by {self.added_by.username}'

