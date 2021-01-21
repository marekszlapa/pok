from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('custom', views.custom, name='custom'),
    path('home', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile', views.profil, name='profile'),
    path('matching', views.matching, name='matching'),
    path('twoje_psy', views.twoje_psy, name='twoje_psy'),
    path('create_dog', views.create_dog, name='create_dog'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'))
    path('password/', views.PasswordChangeView.as_view(template_name='change-password.html'))
]