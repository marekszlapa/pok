# Pokochaj Zwierzaka
Konfiguracja nazwy użytkownika i poczty e-mail:
* > git config --global user.name "Imie Nazwisko"
* > git config --global user.email "email"
  
Aktualizacja bibliotek w pliku requirements.txt:
* wyświetlenie używanych bibliotek i ich wersji:
   >pip list

Instalacja bibliotek:
* > pip install -r requirements.txt
  
Migracja bazy danych:
* > python manage.py makemigrations
* > python manage.py sqlmigrate <nazwa_aplikacji>(pokochaj_zwierzaka) <nazwa_wygenerowanego_pliku>
* > python manage.py migrate