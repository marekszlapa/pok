from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('custom', views.custom, name='custom'),
    path('home', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile', views.profil, name='profile'),
]