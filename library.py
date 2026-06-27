# Aplikacja konsolowa "Biblioteka" — wersja podstawowa
# Wykonana z użyciem wyłącznie programowania strukturalnego (bez klas i importów zewnętrznych)

# ==============================================================================
# STRUKTURY DANYCH (Stan globalny aplikacji zainicjalizowany na sztywno)
# ==============================================================================

# Katalog książek: kluczem jest tytuł, wartością słownik z autorem i liczbą sztuk
katalog_ksiazek = {
    "Władca Pierścieni": {"autor": "J.R.R. Tolkien", "sztuki": 3},
    "Wiedźmin: Ostatnie życzenie": {"autor": "Andrzej Sapkowski", "sztuki": 2},
    "1984": {"autor": "George Orwell", "sztuki": 5},
    "Pan Tadeusz": {"autor": "Adam Mickiewicz", "sztuki": 0},  # 0 sztuk do testowania blokady wypożyczenia
    "Zbrodnia i kara": {"autor": "Fiodor Dostojewski", "sztuki": 4}
}

# Słownik użytkowników: login -> dane (hasło i rola)
uzytkownicy = {
    "jan_nowak": {"haslo": "haslo123", "rola": "czytelnik"},
    "anna_kowalska": {"haslo": "kowal99", "rola": "czytelnik"},
    "piotr_w": {"haslo": "bezpieczne", "rola": "czytelnik"}
}

# Rejestr wypożyczeń: login -> lista wypożyczonych tytułów
wypozyczenia = {
    "jan_nowak": [],
    "anna_kowalska": [],
    "piotr_w": []
}

# ==============================================================================
# FUNKCJE OPERACYJNE
# ==============================================================================

def zaloguj_uzytkownika(baza_uzytkownikow):
    """
    Obsługuje proces logowania użytkownika.
    Użytkownik ma maksymalnie 3 próby na podanie prawidłowych danych.
    Zwraca login po udanym logowaniu lub None w przypadku niepowodzenia.
    """
    print("\n" + "=" * 50)
    print("                LOGOWANIE UŻYTKOWNIKA")
    print("=" * 50)
    
    max_proby = 3
    for proba in range(1, max_proby + 1):
        login = input(f"Podaj login (Próba {proba}/{max_proby}): ").strip()
        haslo = input("Podaj hasło: ")
        
        # Weryfikacja istnienia użytkownika i poprawności hasła
        if login in baza_uzytkownikow and baza_uzytkownikow[login]["haslo"] == haslo:
            print(f"\n[SUKCES] Zalogowano pomyślnie jako: {login}")
            return login
        else:
            print("[BŁĄD] Niepoprawny login lub hasło.\n")
            
    print("[KOMUNIKAT] Przekroczono limit prób logowania. Program zostanie zakończony.")
    return None

def wyswietl_katalog(katalog):
    """
    Wyświetla listę wszystkich książek w katalogu wraz z ich autorami
    oraz liczbą dostępnych sztuk.
    """
    print("\n" + "-" * 60)
    print(f"{'TYTUŁ':<30s} | {'AUTOR':<20s} | {'DOSTĘPNE SZTUKI':<15s}")
    print("-" * 60)
    
    for tytul, info in katalog.items():
        status = f"{info['sztuki']} szt." if info['sztuki'] > 0 else "BRAK SZTUK"
        print(f"{tytul:<30s} | {info['autor']:<20s} | {status:<15s}")
    print("-" * 60)

def wypozycz_ksiazke(login, katalog, rejestr_wypozyczen):
    """
    Umożliwia zalogowanemu użytkownikowi wypożyczenie książki.
    Sprawdza, czy książka istnieje i czy są dostępne sztuki.
    Zmniejsza liczbę sztuk o 1 i dodaje tytuł na listę użytkownika.
    """
    print("\n" + "-" * 50)
    wpisany_tytul = input("Wpisz tytuł książki do wypożyczenia: ").strip()
    
    # Wyszukiwanie książki w katalogu (tolerancyjne na wielkość liter i białe znaki)
    znaleziony_tytul = None
    for tytul_org in katalog.keys():
        if tytul_org.strip().lower() == wpisany_tytul.lower():
            znaleziony_tytul = tytul_org
            break
            
    if not znaleziony_tytul:
        print("[INFO] Nie znaleziono w katalogu książki o podanym tytule.")
        return

    info = katalog[znaleziony_tytul]
    
    # Walidacja liczby sztuk
    if info["sztuki"] > 0:
        # Zmniejszamy stan w katalogu
        info["sztuki"] -= 1
        # Dodajemy do listy wypożyczeń zalogowanego użytkownika
        rejestr_wypozyczen[login].append(znaleziony_tytul)
        print(f"[SUKCES] Wypożyczono książkę: \"{znaleziony_tytul}\"!")
    else:
        print(f"[KOMUNIKAT] Niestety, książka \"{znaleziony_tytul}\" jest obecnie niedostępna (0 sztuk).")

def wyswietl_moje_wypozyczenia(login, rejestr_wypozyczen):
    """
    Wyświetla listę książek wypożyczonych przez aktualnie zalogowanego użytkownika.
    """
    lista_wypozyczen = rejestr_wypozyczen.get(login, [])
    
    print("\n" + "-" * 50)
    print(f"MOJE WYPOŻYCZENIA (Zalogowany: {login}):")
    print("-" * 50)
    
    if not lista_wypozyczen:
        print("Nie masz obecnie żadnych wypożyczonych książek.")
    else:
        for i, tytul in enumerate(lista_wypozyczen, 1):
            print(f"  {i}. {tytul}")
    print("-" * 50)

# ==============================================================================
# GŁÓWNA PĘTLA APLIKACJI
# ==============================================================================

def main():
    # KROK 1: Logowanie użytkownika
    zalogowany_uzytkownik = zaloguj_uzytkownika(uzytkownicy)
    
    # Jeśli logowanie nie powiodło się (zwrócono None), kończymy działanie
    if not zalogowany_uzytkownik:
        return
        
    # KROK 2: Pętla menu głównego
    while True:
        print("\n" + "=" * 50)
        print(f"        MENU BIBLIOTEKI — Zalogowany: {zalogowany_uzytkownik}")
        print("=" * 50)
        print("1. Przeglądaj katalog książek")
        print("2. Wypożycz książkę")
        print("3. Pokaż moje wypożyczenia")
        print("4. Wyloguj i zakończ")
        print("=" * 50)
        
        wybor = input("Wybierz opcję (1-4): ").strip()
        
        if wybor == "1":
            wyswietl_katalog(katalog_ksiazek)
        elif wybor == "2":
            wypozycz_ksiazke(zalogowany_uzytkownik, katalog_ksiazek, wypozyczenia)
        elif wybor == "3":
            wyswietl_moje_wypozyczenia(zalogowany_uzytkownik, wypozyczenia)
        elif wybor == "4":
            print(f"\nWylogowano pomyślnie. Dziękujemy za skorzystanie z biblioteki, {zalogowany_uzytkownik}!")
            break
        else:
            print("[BŁĄD] Wybrano nieprawidłową opcję. Spróbuj ponownie (wpisz cyfrę od 1 do 4).")

if __name__ == "__main__":
    main()
