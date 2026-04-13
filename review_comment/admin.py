from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('title', 'boardgame', 'author', 'rating', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('rating', 'created_at',)
    prepopulated_fields = {}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('review', 'author', 'created_at')
    search_fields = ['content', 'author']
    list_filter = ('created_at',)
    prepopulated_fields = {}
    summernote_fields = ('content',)