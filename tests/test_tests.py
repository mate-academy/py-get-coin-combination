import pytest

from app import main


def test_return_only_pennies(monkeypatch):
    def return_only_pennies(cents: int) -> list:
        return [cents, 0, 0, 0]

    monkeypatch.setattr(main, "get_coin_combination", return_only_pennies)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 1
    ), "Tests should check that 'get_coin_combination' could return different coins, not only pennies"


def test_return_only_one_type(monkeypatch):
    def return_only_one_type(cents: int) -> list:
        if cents < 5:
            return [cents, 0, 0, 0]
        if cents < 10:
            return [0, cents // 5, 0, 0]
        if cents < 25:
            return [0, 0, cents // 10, 0]
        return [0, 0, 0, cents // 25]

    monkeypatch.setattr(main, "get_coin_combination", return_only_one_type)
    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 1
    ), "Tests should check that 'get_coin_combination' could return coins of the different types"
