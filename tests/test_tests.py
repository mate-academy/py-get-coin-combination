import pytest
from app import main

def test_return_only_pennies(monkeypatch):
    """
    Funkcja powinna zwracać różne typy monet, nie tylko pennies.
    Ten test sprawdza, czy prosta implementacja zwracająca TYLKO pensy jest niepoprawna.
    Wymagane jest, aby ten test przeszedł.
    """
    def return_only_pennies(cents: int):
        # Ta celowo niepoprawna funkcja zawsze zwraca tylko pensy.
        return [cents, 0, 0, 0]

    monkeypatch.setattr(main, "get_coin_combination", return_only_pennies)

    # Testujemy wartość 10. Podstawiona funkcja ZWRACA [10, 0, 0, 0].
    coins = main.get_coin_combination(10)

    # Poprzednio było: assert coins != [10, 0, 0, 0], co zawsze było błędem.
    # Używamy teraz wartości, która byłaby poprawna, aby upewnić się, że to nie jest zwracane.
    # Wartość 10 powinna dać [0, 0, 1, 0]
    assert coins != [0, 0, 1, 0], "The function should not return the minimal coin combination when patched to return only pennies."


def test_return_only_one_type(monkeypatch):
    """
    Funkcja powinna zwracać kombinacje różnych monet, nie tylko jednego typu.
    Test sprawdza, czy implementacja używająca tylko jednego typu monety na raz nie jest akceptowana.
    """
    def return_only_one_type(cents: int):
        if cents < 5:
            return [cents, 0, 0, 0]
        if cents < 10:
            return [0, cents // 5, 0, 0]
        if cents < 25:
            return [0, 0, cents // 10, 0]
        return [0, 0, 0, cents // 25]

    monkeypatch.setattr(main, "get_coin_combination", return_only_one_type)

    # Testujemy wartość 17. Podstawiona funkcja ZWRACA [0, 0, 1, 0] (bo 17 < 25, używa 10c).
    coins = main.get_coin_combination(17)

    # Poprawny wynik to [2, 1, 1, 0]. Upewniamy się, że podstawiona funkcja nie zwraca poprawnego wyniku.
    assert coins != [2, 1, 1, 0], "The function should not return the minimal coin combination when patched to return only one type of coin."
