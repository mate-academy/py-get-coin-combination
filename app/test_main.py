from app.main import get_coin_combination


def test_should_return_list_of_zeros_when_cents_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_cent_when_cents_is_one() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_penny_and_dime_when_cents_is_six() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_nickel_and_dime_when_cents_is_fifteen() -> None:
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_should_return_four_zero_two_three_when_cents_is_ninety_nine() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
