from app.main import get_coin_combination


def test_when_only_penny_possible() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_when_one_penny_and_one_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_for_one_dime_and_some_other_coin() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_for_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_for_a_lot_of_coins() -> None:
    assert get_coin_combination(1749) == [4, 0, 2, 69]


def test_should_return_list_with_zeroes_when_input_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
