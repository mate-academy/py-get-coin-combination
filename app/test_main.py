from app.main import get_coin_combination


def test_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_quarter() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
