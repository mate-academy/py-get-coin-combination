from app.main import get_coin_combination


def test_if_amount_equal_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_equal_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_equal_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_equal_penny_and_nickel_and_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_equal_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_for_big_amount() -> None:
    assert get_coin_combination(1000) == [0, 0, 0, 40]


def test_should_return_all_coins() -> None:
    assert get_coin_combination(117) == [2, 1, 1, 4]
