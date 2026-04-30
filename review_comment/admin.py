from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """Admin interface for managing reviews."""

    list_display = ('title', 'boardgame', 'author', 'rating', 'created_at', 'approved')
    search_fields = ['title', 'content']
    list_filter = ('rating', 'created_at', 'approved')
    prepopulated_fields = {}
    summernote_fields = ('content',)
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        """Approve selected reviews."""
        queryset.update(approved=True)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """Admin interface for managing comments."""

    list_display = ('content', 'author', 'created_at', 'approved')
    search_fields = ['content', 'author']
    list_filter = ('created_at', 'approved')
    prepopulated_fields = {}
    summernote_fields = ('content',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Approve selected comments."""
        queryset.update(approved=True)
