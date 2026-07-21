from app.main import get_coin_combination


def test_number_of_pennies() -> None:
    cents = 1
    assert get_coin_combination(cents) == [1, 0, 0, 0]


def test_number_of_nickels() -> None:
    cents = 6
    assert get_coin_combination(cents) == [1, 1, 0, 0]


def test_number_of_dimes() -> None:
    cents = 17
    assert get_coin_combination(cents) == [2, 1, 1, 0]


def test_number_of_quarters() -> None:
    cents = 50
    assert get_coin_combination(cents) == [0, 0, 0, 2]
