from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library_page, name='library_page'),
    path('library/add/<int:boardgame_id>/', views.add_to_library, name='add_to_library'),
    path('library/remove/<int:entry_id>/', views.remove_from_library, name='remove_from_library'),
]