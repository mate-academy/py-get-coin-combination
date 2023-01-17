from app.main import get_coin_combination


def test_number_of_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_number_of_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_number_of_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_number_of_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_number_equals_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
