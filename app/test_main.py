from pytest import raises
from app.main import get_coin_combination


def test_return_zero_list_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_one_penny_for_one_cents() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_nickels_for_cents_more_5() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_return_dimes_for_cents_more_10() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]


def test_return_quarters_for_cents_more_25() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_return_large_numbers_for_large_cents() -> None:
    assert get_coin_combination(4135435543441) == [1, 1, 1, 165417421737]


def test_should_accept_correct_type_arguments() -> None:
    with raises(TypeError):
        get_coin_combination("13")
