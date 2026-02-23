from app.main import get_coin_combination


def test_should_return_a_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_a_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_a_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_a_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
