from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Dog
from .forms import CreateDogForm


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
    return render(request, 'home.html')


def profil(request):
    return render(request, 'profile.html')


def matching(request):
    return render(request, 'matching.html')


def twoje_psy(request):
    return render(request, 'twoje_psy.html')


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
            new_dog = Dog(data_urodzenia=data_urodzenia, rasa=rasa, imie=imie, charakter=charakter, specjalne_potrzeby=specjalne_potrzeby,
                          choroby=choroby, pobyt_w_schronisku=pobyt_w_schronisku, shelter=shelter, fotografia=fotografia)
            new_dog.save()
            # messages.info(request, 'Pomyślnie dodano nowego psa do bazy')
            return redirect('/twoje_psy')
    else:
        create_dog_form = CreateDogForm()
        # messages.info(request, 'Nie udało się dodać nowego psa do bazy')

    return render(request, 'create_dog.html', {'create_dog_form': create_dog_form})
