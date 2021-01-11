from django.forms import ModelForm
from django import forms
from .models import Dog
import datetime


class CreateDogForm(ModelForm):
    AVAILABE_YEARS = ()

    class Meta:
        model = Dog
        fields = ['born', 'breed', 'name', 'character', 'special_needs',
                  'diseases', 'shelter_stay']
        widgets = {
            'born': forms.SelectDateWidget(years=range(1998, datetime.datetime.now().year + 1)),
            'shelter_stay': forms.SelectDateWidget(years=range(1998, datetime.datetime.now().year + 1))
        }
