from django.forms import ModelForm
from django import forms
from .models import Dog
import datetime


class CreateDogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['data_urodzenia', 'rasa', 'imie', 'charakter', 'specjalne_potrzeby',
                  'choroby', 'pobyt_w_schronisku', 'fotografia']
        widgets = {
            'data_urodzenia': forms.SelectDateWidget(years=range(1998, datetime.datetime.now().year + 1)),
            'pobyt_w_schronisku': forms.SelectDateWidget(years=range(1998, datetime.datetime.now().year + 1)),
            'rasa': forms.Select(attrs={'class': 'form-control'}),
            'imie': forms.TextInput(attrs={'class': 'form-control'}),
            'charakter': forms.Textarea(attrs={'class': 'form-control'}),
            'specjalne_potrzeby': forms.Textarea(attrs={'class': 'form-control'}),
            'choroby': forms.Textarea(attrs={'class': 'form-control'})

        }
