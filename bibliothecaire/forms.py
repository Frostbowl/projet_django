from django import forms
from .models import Media

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        champs = ['name', 'disponible', 'date_Emprunt', 'emprunteur']

        def __str__(self):
            return self.nom