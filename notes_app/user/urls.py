from django.urls import path
from notes_app.user.views import profile_info, delete_profile

urlpatterns = [
    path('', profile_info, name='profile'),
    path('delete', delete_profile, name='delete profile'),
]
