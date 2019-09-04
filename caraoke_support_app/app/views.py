from django.shortcuts import render
from .models import Song


def all_song(request):
    songs = Song.objects.order_by('title')
    print('all_song')
    return render(request, 'app/all_song.html', {'songs': songs})
