from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import Dog, Dopasowanie
from .forms import CreateDogForm, CreateDopasowanieForm, PasswordChangingForm
from django.urls import reverse_lazy


# tworzenie widków

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Niewłaściwy login lub hasło')
            return redirect("/")
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, email=email)
        if user is not None:
            messages.info(request, 'Ten użytkownik już istnieje')
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
        return redirect('http://127.0.0.1:8000')
    else:
        return render(request, 'register.html')


def custom(request):
    return render(request, 'custom.html')


def home(request):
    all_dogs = Dog.objects.all
    return render(request, 'home.html', {'all': all_dogs})


def profil(request):
    return render(request, 'profile.html')


def matching(request):
    return render(request, 'matching.html')


def twoje_psy(request):
    all_dogs = Dog.objects.all
    return render(request, 'twoje_psy.html', {'all': all_dogs})


def create_dog(request):
    if request.method == 'POST':
        create_dog_form = CreateDogForm(request.POST, request.FILES)
        if create_dog_form.is_valid():
            data_urodzenia = create_dog_form.cleaned_data['data_urodzenia']
            rasa = create_dog_form.cleaned_data['rasa']
            imie = create_dog_form.cleaned_data['imie']
            charakter = create_dog_form.cleaned_data['charakter']
            specjalne_potrzeby = create_dog_form.cleaned_data['specjalne_potrzeby']
            choroby = create_dog_form.cleaned_data['choroby']
            shelter = request.user
            pobyt_w_schronisku = create_dog_form.cleaned_data['pobyt_w_schronisku']
            fotografia = create_dog_form.cleaned_data['fotografia']
            new_dog = Dog(data_urodzenia=data_urodzenia, rasa=rasa, imie=imie, charakter=charakter,
                          specjalne_potrzeby=specjalne_potrzeby,
                          choroby=choroby, pobyt_w_schronisku=pobyt_w_schronisku, shelter=shelter,
                          fotografia=fotografia)
            new_dog.save()
            # messages.info(request, 'Pomyślnie dodano nowego psa do bazy')
            return redirect('/twoje_psy')
    else:
        create_dog_form = CreateDogForm()
        # messages.info(request, 'Nie udało się dodać nowego psa do bazy')

    return render(request, 'create_dog.html', {'create_dog_form': create_dog_form})


def matching(request):
    if request.method == 'POST':
        create_dopasowanie_form = CreateDopasowanieForm(request.POST)
        if create_dopasowanie_form.is_valid():
            wiek_psa = create_dopasowanie_form.cleaned_data['wiek_psa']
            rasa_psa = create_dopasowanie_form.cleaned_data['rasa_psa']
            czas_pobytu_w_schronisku = create_dopasowanie_form.cleaned_data['czas_pobytu_w_schronisku']
            pies_ze_specjalnymi_wymaganiami = create_dopasowanie_form.cleaned_data['pies_ze_specjalnymi_wymaganiami']
            pies_z_chorobami = create_dopasowanie_form.cleaned_data['pies_z_chorobami']
            uzytkownik = request.user
            new_dopasowanie = Dopasowanie(wiek_psa=wiek_psa, rasa_psa=rasa_psa,
                                          czas_pobytu_w_schronisku=czas_pobytu_w_schronisku,
                                          pies_ze_specjalnymi_wymaganiami=pies_ze_specjalnymi_wymaganiami,
                                          pies_z_chorobami=pies_z_chorobami,
                                          uzytkownik=uzytkownik)
            new_dopasowanie.save()
            # messages.info(request, 'Pomyślnie dodano nowego psa do bazy')
            return redirect('/home')
    else:
        create_dopasowanie_form = CreateDopasowanieForm()
        # messages.info(request, 'Nie udało się dodać nowego psa do bazy')

    return render(request, 'matching.html', {'create_dopasowanie_form': create_dopasowanie_form})


class PasswordChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
