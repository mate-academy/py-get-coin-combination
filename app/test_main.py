import pytest

from app.main import get_coin_combination


def test_should_return_empty_list_if_coins_are_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_pennie() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_list_of_ones() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_raise_error_is_coins_are_not_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("coins")
