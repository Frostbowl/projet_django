from django.shortcuts import render
from bibliothecaire.models import Media

def media_list(request):
    medias = Media.objects.all()
    return render(request, 'consultation/media_list.html', {'medias': medias})