Instalacja i Uruchomienie

    Klonowanie repozytorium

git clone https://github.com/twoj-uzytkownik/portfolio.git
cd portfolio

git clone https://github.com/twoj-uzytkownik/portfolio.git
cd portfolio

Instalacja zależności
Upewnij się, że masz zainstalowanego Pythona 3.6+ oraz pip. Następnie zainstaluj zależności:

pip install Flask SQLAlchemy

Inicjalizacja bazy danych
Uruchom skrypt inicjalizujący bazę danych:

python init_db.py

Uruchomienie aplikacji

python app.py

Aplikacja będzie dostępna pod adresem http://127.0.0.1:5000/


Użycie

    Strona główna
    Strona główna wyświetla informacje o użytkowniku oraz jego umiejętnościach. Informacje te można edytować przez panel administracyjny.

    Logowanie
    Aby zalogować się jako administrator, przejdź na stronę http://127.0.0.1:5000/login i użyj domyślnych danych logowania:
        Username: admin
        Password: admin

    Panel administracyjny
    Po zalogowaniu się jako administrator, przejdź na stronę http://127.0.0.1:5000/admin, gdzie możesz edytować informacje o sobie oraz dodawać nowe umiejętności.

Baza Danych
Modele Danych

    User: Przechowuje informacje o użytkownikach.
        id: int, klucz główny
        username: string, unikalny, niepusty
        password: string, niepusty

    Content: Przechowuje treści wyświetlane na stronie.
        id: int, klucz główny
        about_me: text, niepusty

    Skill: Przechowuje informacje o umiejętnościach użytkownika.
        id: int, klucz główny
        name: string, unikalny, niepusty
        info: string, niepusty
        image: string, niepusty

Funkcje Kluczowe

    Login i Sesje
    Aplikacja wykorzystuje sesje do zarządzania stanem zalogowania użytkownika. Funkcja login_required służy do zabezpieczenia tras wymagających autoryzacji.

    Panel Administracyjny
    Panel administracyjny pozwala na edycję treści strony oraz umiejętności użytkownika. Obsługuje przesyłanie plików graficznych do umiejętności.

    Wyświetlanie Treści
    Strona główna wyświetla informacje o użytkowniku oraz jego umiejętnościach w przystępny sposób, umożliwiając łatwe zarządzanie i aktualizację treści.
    Ten projekt jest idealnym miejscem do nauki i eksperymentowania z Flaskiem oraz podstawami tworzenia aplikacji webowych. Zachęcamy do klonowania, modyfikowania i dzielenia się swoimi usprawnieniami!
