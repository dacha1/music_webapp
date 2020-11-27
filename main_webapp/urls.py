from django.contrib import admin
from django.urls import path
from main_webapp import views


urlpatterns = [
    path('', views.index, name="home"),
    path('artist/<int:artist_id>', views.artist_details, name="artist_detail"),
    path('artist', views.artist_list, name="artist_list")
]
