from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist

# Create your views here.


def index(request):
    artists_list = Artist.objects.all()
    return render(request, 'index.html', {'artists_list': artists_list})
