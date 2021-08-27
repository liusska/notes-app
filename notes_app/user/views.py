from django.shortcuts import render, redirect

from notes_app.core.profile import get_profile
from notes_app.note.models import Note


def profile_info(request):
    profile = get_profile()
    notes = Note.objects.all()
    count_notes = len(notes)
    context = {
        'profile': profile,
        'notes': notes,
        'count_notes': count_notes
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('home')


