from django.shortcuts import render
from .models import Media

# Create your views here.

def layout(request):
    medias = Media.objects
    return render(request, 'app/layout.html', {'medias': medias})
