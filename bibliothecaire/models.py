from django.db import models

class Emprunteur(models.Model):
    nom = models.CharField(max_length=155)
    prenom = models.CharField(max_length=155)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nom} {self.prenom}'
    
    def nombre_emprunt(self):
        return self.media_emprunt.filter(disponible=False).count()
    
    def peut_emprunter(self):
        return self.nombre_emprunt() < 3

    def emprunter_media(self, media):
        if self.peut_emprunter():
            media.disponible = False
            media.emprunteur = self
            media.save()
        else:
            raise ValueError("Cet emprunteur a déjà 3 emprunts en cours.")

class Media(models.Model):
    name = models.CharField(max_length=155)
    disponible = models.BooleanField(default=True)
    date_emprunt = models.DateField(null=True, blank=True)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.SET_NULL, null=True, blank=True, related_name='media_emprunt')

    def get_media_type(self):
        return self.__class__.__name__

class Livre(Media):
    auteur = models.CharField(max_length=155)

class Cd(Media):
    artiste = models.CharField(max_length=155)

class Dvd(Media):
    realisateur = models.CharField(max_length=155)

