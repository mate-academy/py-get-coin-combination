from app.main import get_coin_combination


def test_given_the_smallest_value() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_given_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_given_penny_and_nickel_and_dime() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_given_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_given_nickel_and_quarter() -> None:
    assert get_coin_combination(35) == [0, 0, 1, 1]


def test_given_penny_and_nickel_and_quarter() -> None:
    assert get_coin_combination(40) == [0, 1, 1, 1]


def test_given_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
