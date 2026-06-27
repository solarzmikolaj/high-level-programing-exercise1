# Test integracyjny aplikacji Biblioteka
# Symuluje interakcję użytkownika poprzez zmakowanie funkcji input()

import builtins
import library

# Predefiniowane odpowiedzi użytkownika w symulacji:
inputs = [
    # 1. Logowanie: Udane zalogowanie jako jan_nowak
    "jan_nowak", "haslo123",
    
    # 2. Opcja menu 1: Przeglądanie katalogu książek
    "1",
    
    # 3. Opcja menu 2: Wypożyczenie książki "1984" (która ma 5 sztuk)
    "2", "1984",
    
    # 4. Opcja menu 1: Przeglądanie katalogu po wypożyczeniu (ilość "1984" powinna spaść do 4)
    "1",
    
    # 5. Opcja menu 2: Próba wypożyczenia książki "Pan Tadeusz" (która ma 0 sztuk)
    "2", "Pan Tadeusz",
    
    # 6. Opcja menu 3: Sprawdzenie własnych wypożyczeń (powinna być tam tylko książka "1984")
    "3",
    
    # 7. Opcja menu: Wpisanie błędnej opcji (np. "9")
    "9",
    
    # 8. Opcja menu 4: Wylogowanie i wyjście
    "4"
]

input_index = 0

def mock_input(prompt=""):
    global input_index
    if input_index >= len(inputs):
        return "4"  # Bezpiecznik: jeśli skończą się dane, wyloguj
    val = inputs[input_index]
    # Wypisujemy w konsoli to co "wpisał" użytkownik, by log był czytelny
    print(f"{prompt}\033[94m{val}\033[0m")
    input_index += 1
    return val

# Podmieniamy funkcję input na nasz mock
builtins.input = mock_input

def run_simulation():
    # Przywracamy domyślny stan struktur danych przed testem
    library.katalog_ksiazek = {
        "Władca Pierścieni": {"autor": "J.R.R. Tolkien", "sztuki": 3},
        "Wiedźmin: Ostatnie życzenie": {"autor": "Andrzej Sapkowski", "sztuki": 2},
        "1984": {"autor": "George Orwell", "sztuki": 5},
        "Pan Tadeusz": {"autor": "Adam Mickiewicz", "sztuki": 0},
        "Zbrodnia i kara": {"autor": "Fiodor Dostojewski", "sztuki": 4}
    }
    library.wypozyczenia = {
        "jan_nowak": [],
        "anna_kowalska": [],
        "piotr_w": []
    }
    
    print("\n" + "#" * 70)
    print("   URUCHAMIANIE AUTOMATYCZNEGO TESTU INTEGRACYJNEGO BIBLIOTEKI")
    print("#" * 70)
    
    library.main()
    
    print("\n" + "#" * 70)
    print("   AUTOMATYCZNY TEST ZAKOŃCZONY POMYŚLNIE")
    print("#" * 70)

if __name__ == "__main__":
    run_simulation()
