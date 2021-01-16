from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DISEASE(models.Model):
    disease = models.CharField(max_length=30,unique=True)

class Dog(models.Model):
    BREEDS_AVAILABLE = (
        ('ON', 'owczarek niemiecki'),
        ('LR', 'labrador retriever'),
        ('YR', 'yorkshire terrier'),
        ('SM', 'sznaucer miniaturowy'),
        ('BF', 'buldog francuski'),
    )

    data_urodzenia = models.DateField()
    rasa = models.CharField(max_length=2, choices=BREEDS_AVAILABLE)
    imie = models.CharField(max_length=30)
    charakter = models.TextField(max_length=1024)
    specjalne_potrzeby = models.TextField(max_length=1024, null=True, default=None, blank=True)
    choroby = models.TextField(max_length=1024, null=True, default=None, blank=True)
    pobyt_w_schronisku = models.DateField()
    shelter = models.ForeignKey(User, on_delete=models.CASCADE)
    fotografia = models.ImageField(upload_to='static/images/dogsphotos/', null=True, default=None, blank=True)

    def __str__(self):
        return self.imie

class Dopasowanie(models.Model):
    PRZEDZIALY_WIEKOWE = (
        ('P1', 'do 1 roku'),
        ('P2', 'od 1 do 3 lat'),
        ('P3', 'od 3 do 5 lat'),
        ('P4', 'od 5 do 10 lat'),
        ('P5', 'ponad 10 lat'),
    )

    RASY = (
        ('ON', 'owczarek niemiecki'),
        ('LR', 'labrador retriever'),
        ('YR', 'yorkshire terrier'),
        ('SM', 'sznaucer miniaturowy'),
        ('BF', 'buldog francuski'),
    )

    POBYT_SCHRONISKO = (
        ('P1', 'do 1 roku'),
        ('P2', 'od 1 do 3 lat'),
        ('P3', 'od 3 do 5 lat'),
        ('P4', 'od 5 do 10 lat'),
        ('P5', 'ponad 10 lat'),
    )

    WYBOR = {
        ('T', 'tak'),
        ('N','nie'),
    }

    wiek_psa = models.CharField(max_length=2, choices=PRZEDZIALY_WIEKOWE, null=True, blank=True)
    rasa_psa = models.CharField(max_length=2, choices=RASY, null=True, blank=True)
    czas_pobytu_w_schronisku = models.CharField(max_length=2, choices=POBYT_SCHRONISKO, null=True, blank=True)
    pies_ze_specjalnymi_wymaganiami = models.CharField(max_length=1, choices=WYBOR, null=False, default='T', blank=False)
    pies_z_chorobami = models.CharField(max_length=1, choices=WYBOR, null=False, default='T', blank=False)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rasa_psa

