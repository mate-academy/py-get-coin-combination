from app.main import get_coin_combination


def test_given_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_given_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_given_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_given_penny_and_nickel_and_dime() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_given_penny_and_nickel_and_dime_and_quarter() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
