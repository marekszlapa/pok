from django.forms import ModelForm
from django import forms
from .models import Dog, Dopasowanie
import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


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


class CreateDopasowanieForm(ModelForm):
    class Meta:
        model = Dopasowanie
        fields = ['wiek_psa', 'rasa_psa', 'czas_pobytu_w_schronisku', 'pies_ze_specjalnymi_wymaganiami',
                  'pies_z_chorobami']
        widgets = {
            'wiek_psa': forms.Select(attrs={'class': 'form-control'}),
            'rasa_psa': forms.Select(attrs={'class': 'form-control'}),
            'czas_pobytu_w_schronisku': forms.Select(attrs={'class': 'form-control'}),
            'pies_ze_specjalnymi_wymaganiami': forms.Select(attrs={'class': 'form-control'}),
            'pies_z_chorobami': forms.Select(attrs={'class': 'form-control'})
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
