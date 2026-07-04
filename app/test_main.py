from app.main import get_coin_combination


def cents_should_return_list_of_zero_if_cents_zero() -> None:
    res = get_coin_combination(0)
    assert res == [0, 0, 0, 0]


def test_should_return_quarter_if_cents_25() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_one_penny_and_one_nickel_if_cents_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_one_penny_and_one_dime_if_cents_11() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_should_return_two_dime_and_one_quarter_if_cents_45() -> None:
    assert get_coin_combination(45) == [0, 0, 2, 1]


def test_should_return_one_of_each_coin_if_cents_41() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
