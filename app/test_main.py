from app.main import get_coin_combination


def test_should_return_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_correct_combination() -> None:
    assert get_coin_combination(18) == [3, 1, 1, 0]
