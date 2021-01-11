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

    born = models.DateField()
    breed = models.CharField(max_length=2, choices=BREEDS_AVAILABLE)
    name = models.CharField(max_length=30)
    character = models.TextField(max_length=1024)
    special_needs = models.TextField(max_length=1024)
    diseases = models.TextField(max_length=1024)
    shelter_stay = models.DateField()
    shelter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

