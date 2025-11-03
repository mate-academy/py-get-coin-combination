import pytest
from app.main import get_coin_combination


def test_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel_one_penny():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_dime_nickel_pennies():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_value():
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_only_dimes():
    assert get_coin_combination(30) == [0, 0, 3, 0]


def test_only_nickels():
    assert get_coin_combination(20) == [0, 4, 0, 0]


def test_boundary_values():
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(26) == [1, 0, 0, 1]


def test_negative_raises_error():
    with pytest.raises(ValueError):
        get_coin_combination(-1)
