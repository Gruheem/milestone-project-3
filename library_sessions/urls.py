from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library_page, name='library_page'),
    path('library/add/<int:boardgame_id>/', views.add_to_library, name='add_to_library'),
    path('library/remove/<int:entry_id>/', views.remove_from_library, name='remove_from_library'),
    path('library/<int:entry_id>/sessions/', views.play_session_page, name='play_session_page'),
]