from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    nationality = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics', blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    soundcloud = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)


class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_art = models.ImageField(upload_to='album', blank=True)


