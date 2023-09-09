import pytest

from app.main import get_coin_combination


def test_add_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_add_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_add_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_add_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_return_all_zero_if_no_input() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_return_combination_of_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
