from app.coin_combination import get_coin_combination
import pytest


def test_should_raise_ValueError_when_input_not_int():
    with pytest.raises(TypeError):
        assert get_coin_combination("15")


def test_should_return_zeroes_whin_zero_input():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_only_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_pennies_and_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_pennies_nickel_and_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_pennies_nickel_dime_and_quater():
    assert get_coin_combination(42) == [2, 1, 1, 1]



