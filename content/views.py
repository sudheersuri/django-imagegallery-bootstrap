from django.shortcuts import render
from django.views.generic import ListView
from .models import ArtistImages

class ImagesView(ListView):
    model=ArtistImages
    template_name='home.html'
    