from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Dog
from .forms import CreateDogForm

#tworzenie widków

def index(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/home')
        else:
            messages.info(request, 'Niewłaściwy login lub hasło')
            return redirect("/")
    else:
        return render(request,'index.html')


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']


        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
        return redirect('http://127.0.0.1:8000')

    return render(request,'register.html')

def custom(request):
    return render(request, 'custom.html')


def home(request):
    return render(request, 'home.html')

def profil(request):
    return render(request, 'profile.html')

def matching(request):
    return render(request, 'matching.html')

def create_dog(request):
    if request.method == 'POST':
        create_dog_form = CreateDogForm(request.POST)
        if create_dog_form.is_valid():
            born = create_dog_form.cleaned_data['born']
            breed = create_dog_form.cleaned_data['breed']
            name = create_dog_form.cleaned_data['name']
            character = create_dog_form.cleaned_data['character']
            special_needs = create_dog_form.cleaned_data['special_needs']
            diseases = create_dog_form.cleaned_data['diseases']
            shelter = request.user
            shelter_stay = create_dog_form.cleaned_data['shelter_stay']

            new_dog = Dog(born=born,breed=breed,name=name,character=character,special_needs=special_needs,
                          diseases=diseases,shelter_stay=shelter_stay,shelter=shelter)
            new_dog.save()
            messages.info(request, 'Pomyślnie dodano nowego psa do bazy')
            return redirect('/profile')
    else:
        create_dog_form = CreateDogForm()
        messages.info(request, 'Nie udało się dodać nowego psa do bazy')

    return render(request, 'create_dog.html',{'create_dog_form':create_dog_form})