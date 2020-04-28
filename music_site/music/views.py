from django.shortcuts import render

from .models import * 

def home(request):
    context = {
        'artists': Musician.objects.all()
    }
    return render(request, 'music/home.html', context)

def artist_detail(request, musician_id):
    context = {
        'artist': Musician.objects.get(id=musician_id)
    }
    return render(request, 'music/detail.html', context)

def album_detail(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id)
    }
    return render(request, 'music/album_detail.html', context)

def song_details(request, song_id):
    context = {
        'song': Song.objects.get(id=song_id)
    }
    return render(request, 'music/song_detail.html', context)