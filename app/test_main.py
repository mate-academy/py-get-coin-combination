from app.main import get_coin_combination


def test_should_return_list_of_four_zeroes_when_zero_cent_given() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_valid_amount_of_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_biggest_coins_first() -> None:
    assert get_coin_combination(42) == [2, 1, 1, 1]


def test_should_return_only_quarters_when_cent_divided_by_25() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
