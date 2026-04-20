from django.contrib import admin
from .models import Genre, BoardGame
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(BoardGame)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'approved', 'status', 'created_at')
    search_fields = ['title', 'description']
    list_filter = ('approved', 'status', 'created_at',)
    prepopulated_fields = {}
    summernote_fields = ('description',)
    actions = ['approve_games']

    def approve_games(self, request, queryset):
        queryset.update(approved=True)
        
    approve_games.short_description = 'Approve selected games'


admin.site.register(Genre)