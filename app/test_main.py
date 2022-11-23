from app.main import get_coin_combination


def test_value_should_be_greater_than_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_result_should_return_different_coins_not_only_pennies() -> None:
    assert get_coin_combination(7) == [2, 1, 0, 0]


def test_result_should_return_coins_of_different_value() -> None:
    assert get_coin_combination(43) == [3, 1, 1, 1]
