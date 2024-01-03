from app.main import get_coin_combination


def test_result_should_be_pennies_when_cents_less_than_5() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_result_should_be_only_nickels_when_cents_equals_to_5() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_result_should_be_pennies_and_nickels_when_less_than_10() -> None:
    assert get_coin_combination(8) == [3, 1, 0, 0]


def test_result_only_dimes_when_cents_less_then_25_and_divided_by_10() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_should_be_pennies_nickels_and_dimes_when_less_than_25() -> None:
    assert get_coin_combination(18) == [3, 1, 1, 0]


def test_result_should_be_only_quarters_when_divisible_by_25() -> None:
    assert get_coin_combination(175) == [0, 0, 0, 7]


def test_should_be_all_coins_when_cents_greater_than_sum_of_coins() -> None:
    assert get_coin_combination(69) == [4, 1, 1, 2]


def test_result_should_be_zeros_when_cents_equal_to_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
