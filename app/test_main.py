from app.main import get_coin_combination


def test_should_return_zero_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_penny_for_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_nickel_and_one_penny_for_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_two_pennies_one_nickel_one_dime_for_seventeen() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_two_quarters_for_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_max_combination_with_all_coin_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
