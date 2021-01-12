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

