import pytest
from app.main import get_coin_combination

def test_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]

def test_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]

def test_one_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]

def test_one_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]

def test_mixed_coins():
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]

def test_large_amount():
    assert get_coin_combination(99) == [4, 0, 2, 3]
