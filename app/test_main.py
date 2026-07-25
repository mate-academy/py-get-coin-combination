from app.main import get_coin_combination


def test_should_return_zero_if_zero_given() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_two_penny_and_nickel() -> None:
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_should_return_dime_nickel_and_penny() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_two_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_should_return_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_can_return_different_coins() -> None:
    assert get_coin_combination(68) == [3, 1, 1, 2]
