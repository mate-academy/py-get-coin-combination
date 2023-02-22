from app.main import get_coin_combination
import pytest

def test_should_return_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_penny_and_one_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_two_pennies_one_nickel_and_one_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_two_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]

