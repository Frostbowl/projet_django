from django.db import models

class Livre(models.Model):
    name = models.CharField(max_length=155)
    auteur = models.CharField(max_length=155)
    disponible = models.BooleanField(default=True)

class Dvd(models.Model):
    name = models.CharField(max_length=150)
    realisateur = models.CharField(max_length=150)
    disponible = models.BooleanField(default=True)

class Cd(models.Model):
    name = models.CharField(max_length=150)
    artiste = models.CharField(max_length=150)
    disponible = models.BooleanField(default=True)

class JeuPlateau(models.Model):
    name = models.CharField(max_length=155)
    createur = models.CharField(max_length=155)
    disponible = models.BooleanField(default=True)

class Membre(models.Model):
    nom = models.CharField(max_length=155)
    prenom = models.CharField(max_length=155)
    bloque = models.BooleanField(default=False)

class Emprunt(models.Model):
    media_choix = [
        ('livre', 'Livre'),
        ('cd', 'CD'),
        ('dvd', 'DVD'),
    ]

    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=155, choix=media_choix)
    media_id = models.PositiveIntegerField()
    media_name = models.CharField(max_length=155, default="unknow")

    def __str__(self):
        return f'{self.membre} emprunte {self.media_type}{self.media_id}{self.media_name}'