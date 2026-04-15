from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library_page, name='library_page'),
#     path('add/<int:boardgame_id>/', views.add_to_library, name='add_to_library'),
#     path('remove/<int:entry_id>/', views.remove_from_library, name='remove_from_library'),
]