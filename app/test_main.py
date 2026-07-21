import pytest
from app.main import get_coin_combination


def test_function_returns_a_list_of_four_elements() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_zeros_if_get_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_when_anml_year_less_than_sum_1_2_h_year() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_raise_error_if_function_get_non_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("25 cents")
