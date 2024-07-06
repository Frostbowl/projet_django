from django.shortcuts import render, redirect, get_object_or_404
from .models import Media, Emprunteur
from .forms import MediaTypeForm, LivreForm, CdForm, DvdForm, EmprunteurForm

def choix_media_type(request):
    if request.method == 'POST':
        form = MediaTypeForm(request.POST)
        if form.is_valid():
            media_type = form.cleaned_data['media_type']
            return redirect ('ajout_media', media_type=media_type)

    else:
        form = MediaTypeForm()
    return render(request, 'bibliothecaire/choix_media_type.html', {'form':form})

def ajout_media(request, media_type):
    if media_type == 'Livre':
        FormClass = LivreForm
    elif media_type == 'Cd':
        FormClass = CdForm
    elif media_type == 'Dvd':
        FormClass = DvdForm
    else:
        return redirect('choix_media_type')
    
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = FormClass()

    return render(request, 'bibliothecaire/ajout_media.html', {'form': form, 'media_type': media_type })


def media_list(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/media_list.html', {'medias': medias})


def create_emprunteur(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprunteur_list')
    
    else:
        form = EmprunteurForm()
        return render (request, 'bibliothecaire/create_emprunteur.html', {'form': form})

def emprunteur_list(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/emprunteur_list.html', {'emprunteurs': emprunteurs})


def emprunter_media(request, emprunteur_id, media_id):
    emprunteur = get_object_or_404(Emprunteur, pk=emprunteur_id)
    media = get_object_or_404(Media, pk=media_id)

    try:
        emprunteur.emprunter_media(media)
        return redirect('media_list')
    except ValueError as e:
        return render(request, 'bibliothecaire/emprunteur_error.html', {'error_message': str(e)})
