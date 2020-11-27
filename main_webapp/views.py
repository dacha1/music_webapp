from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Album

# Create your views here.


def index(request):
    artists_list = Artist.objects.all()
    return render(request, 'index.html', {'artists_list': artists_list})

def artist_details(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    albums = Album.objects.all().filter(artist_id=artist.pk)

    return render(request, 'artist_details.html', {'albums': albums, 'artist': artist})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})

