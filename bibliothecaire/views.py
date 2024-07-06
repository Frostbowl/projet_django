from django.shortcuts import render
from .models import Media


def media_list(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/media_list.html', {'medias': medias})
