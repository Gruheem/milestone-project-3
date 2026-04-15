from django.contrib import admin
from .models import LibraryEntry

# Register your models here.
@admin.register(LibraryEntry)
class LibraryEntryAdmin(admin.ModelAdmin):

    list_display = ('user', 'boardgame', 'status', 'added_at')
    search_fields = ['user__username', 'boardgame__name'] # Double underscore to search related fields
    list_filter = ('status', 'added_at')