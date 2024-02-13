from django.db import models

# Create your models here.
class Salle(models.Model):
    nom = models.CharField(max_length=255)
    capacite = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    nom = models.CharField(max_length=255)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.nom
