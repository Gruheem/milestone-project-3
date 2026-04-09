from django.contrib import admin
from .models import Genre, BoardGame
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(BoardGame)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_at')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_at',)
    prepopulated_fields = {}
    summernote_fields = ('description',)

admin.site.register(Genre)