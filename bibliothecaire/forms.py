from django import forms
from .models import Media, Livre, Cd, Dvd, Emprunteur

class MediaTypeForm(forms.Form):
    media_type = forms.ChoiceField(choices=[
        ('Livre', 'LIVRE'),
        ('Cd', 'CD'),
        ('Dvd', 'DVD'),
    ])

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'disponible', 'date_emprunt', 'emprunteur']
        
class LivreForm(MediaForm):
    class Meta(MediaForm.Meta):
        model = Livre
        fields = MediaForm.Meta.fields + ['auteur']

class CdForm(MediaForm):
    class Meta(MediaForm.Meta):
        model = Cd
        fields = MediaForm.Meta.fields + ['artiste']

class DvdForm(MediaForm):
    class Meta(MediaForm.Meta):
        model = Dvd
        fields = MediaForm.Meta.fields + ['realisateur']

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['nom', 'prenom', 'bloque']