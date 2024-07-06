from django.urls import path
from .views import choix_media_type, ajout_media, media_list, create_emprunteur, emprunteur_list
from . import views

urlpatterns = [
    path('', media_list, name='media_list'),
    path('choix_media_type/', choix_media_type, name='choix_media_type'),
    path('ajout_media/<str:media_type>/', ajout_media, name='ajout_media'),
    path('create_emprunteur/', create_emprunteur, name='create_emprunteur'),
    path('emprunteur_list/', emprunteur_list, name='emprunteur_list'),
    path('emprunteur/<int:emprunteur_id>/media/<int:media_id>/emprunter/', views.emprunter_media, name='emprunter_media'),
]
