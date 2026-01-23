from app.main import get_coin_combination


def test_return_zeroes_if_cents_equals_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_1_penny_if_cents_equals_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_a_nickel_if_cents_equals_5_and_more() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_return_a_dime_if_cents_equals_15_and_more() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_return_a_quarter_if_cents_equals_25_and_more() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]
