from app.main import get_coin_combination


def test_should_return_list_of_zeros_when_cents_is_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_cent_when_cents_is_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_penny_and_dime_when_cents_is_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_nickel_and_dime_when_cents_is_15() -> None:
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_should_return_expected_result_when_cents_is_99() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
