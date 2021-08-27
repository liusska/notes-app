from django.urls import path

from notes_app.note.views import home
from notes_app.note.views import add_note
from notes_app.note.views import edit_note
from notes_app.note.views import delete_note
from notes_app.note.views import details_note
from notes_app.note.views import create_profile


urlpatterns = [
    path('', home, name='home'),
    path('create', create_profile, name='create profile'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),
]