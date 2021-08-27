from notes_app.user.models import Profile


def get_profile():
    return Profile.objects.first()
