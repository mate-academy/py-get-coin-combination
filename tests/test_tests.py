# tests/test_tests.py
import pytest
from app import main

def test_return_only_pennies(monkeypatch):
    """
    Funkcja powinna zwracać różne typy monet, nie tylko pennies.
    """
    def return_only_pennies(cents: int):
        return [cents, 0, 0, 0]  # sztuczna funkcja zwracająca tylko pennies

    monkeypatch.setattr(main, "get_coin_combination", return_only_pennies)

    # Testujemy kilka wartości
    coins = main.get_coin_combination(10)
    assert coins != [10, 0, 0, 0], "Function should return other coins, not only pennies"

def test_return_only_one_type(monkeypatch):
    """
    Funkcja powinna zwracać kombinacje różnych monet, nie tylko jednego typu.
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

    coins = main.get_coin_combination(17)
    assert coins != [0, 0, 1, 0], "Function should return combination of different coins"
