from app.main import get_coin_combination


def test_returns_penny_if_total_value_is_less_than_5() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_returns_nickel_if_total_value_between_5_and_10() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_returns_dime_if_total_value_between_10_and_25() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_returns_quarter_if_total_value_is_greater_than_25() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
