import pytest

from app.main import get_coin_combination


def test_should_return_list_of_zeros_when_zero_passed_in() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_correct_combination_if_passed_nonnegative_num() -> None:
    assert get_coin_combination(49) == [4, 0, 2, 1]


def test_should_return_float_type_if_float_is_passed_in() -> None:
    assert get_coin_combination(23.5) == [3.0, 0.0, 2.0, 0.0]


def test_should_raise_error_when_passed_other_type_then_numbers() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("bad_type")
