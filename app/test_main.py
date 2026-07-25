import pytest

from app.main import get_coin_combination


def test_should_output_four_elements() -> None:
    assert len(get_coin_combination(0)) == 4


def test_should_check_zero_combination() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_display_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_display_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_display_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_display_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_all_coin_combination() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_raise_error_if_arguments_is_string() -> None:
    with pytest.raises(TypeError):
        assert get_coin_combination("41")


def test_should_return_combination_for_big_number() -> None:
    assert get_coin_combination(1469) == [4, 1, 1, 58]
