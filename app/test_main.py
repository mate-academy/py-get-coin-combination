from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_different_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
