from app.main import get_coin_combination


def test_amount_of_penalty() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_amount_of_nickels_and_pennies() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_amount_of_pennies_nikel_and_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_amount_of_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
