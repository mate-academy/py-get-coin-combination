from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_penny_one_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_penny_nickel_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_when_nickel_zero() -> None:
    assert get_coin_combination(49) == [4, 0, 2, 1]
