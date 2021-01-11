from django.forms import ModelForm
from django import forms
from .models import Dog
import datetime


class CreateDogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['born', 'breed', 'name', 'character', 'special_needs',
                  'diseases', 'shelter_stay', 'photo']
        widgets = {
            'born': forms.SelectDateWidget(years=range(1998, datetime.datetime.now().year + 1)),
            'shelter_stay': forms.SelectDateWidget(years=range(1998, datetime.datetime.now().year + 1)),
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'character': forms.Textarea(attrs={'class': 'form-control'}),
            'special_needs': forms.Textarea(attrs={'class': 'form-control'}),
            'diseases': forms.Textarea(attrs={'class': 'form-control'})

        }
