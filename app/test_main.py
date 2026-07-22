import pytest
from app.main import get_coin_combination


def test_should_return_number_of_pennies_when_cents_are_less_5() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_number_of_nickels_when_cents_are_less_10() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_number_of_dimes_when_cents_are_less_25() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_number_of_quarters_when_cents_are_greater_than_24()\
        -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_zeros_when_cents_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_expected_result_when_data_is_negative_number() -> None:
    assert get_coin_combination(-5) == [0, 0, 2, -1]


def test_should_return_expected_result_when_data_is_large_number() \
        -> None:
    assert get_coin_combination(269) == [4, 1, 1, 10]


def test_should_raise_error_if_data_is_str() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("45")
