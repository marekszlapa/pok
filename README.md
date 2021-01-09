# Pokochaj Zwierzaka
**Konfiguracja nazwy użytkownika i poczty e-mail:**
* > git config --global user.name `<Imie Nazwisko>`
* > git config --global user.email `<email>`
  
**Git - przydatne komendy:**
* > git status #status plików
* > git pull #update lokalnego brancha ze zdalnego
* > git add `<nazwa pliku z rozszerzeniem>` #dodanie pliku do brancha
* > git commit -m"`<treść komunikatu>`" #ustawianie commita
* > git push #wysłanie plików na zdalne repo
  
**Aktualizacja bibliotek w pliku requirements.txt:**
* należy uruchomić plik activate.bat
  >venv\Scripts\activate.bat
* wyświetlenie używanych bibliotek i ich wersji:
   >pip list

**Instalacja bibliotek:**
* należy uruchomić plik activate.bat
  >venv\Scripts\activate.bat
* instalacja wszystkich bilbiotek z pliku requirements.txt:
  > pip install -r requirements.txt
  
**Migracja bazy danych:**
* > python manage.py makemigrations
* > python manage.py sqlmigrate `<nazwa_aplikacji>`(pokochaj_zwierzaka) `<nazwa_wygenerowanego_pliku>`
* > python manage.py migrate
