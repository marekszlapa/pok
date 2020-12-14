from django.db import models


# Create your models here.
# tworzenie przykladowej tabeli uzytkownika

class UzytkownikPodstawa(models.Model):
    login = models.CharField(max_length=20)
    haslo = models.CharField(max_length=20)
