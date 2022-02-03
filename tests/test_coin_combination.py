import pytest

from app.coin_combination import get_coin_combination


def test_penny():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_dime():
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_all_coins():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_when_coin_is_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    'coin, expected',
    [
        (12, [2, 0, 1, 0]),
        (32, [2, 1, 0, 1]),
        (101, [1, 0, 0, 4])
    ]
)
def test_different_combinations_of_coins(coin, expected):
    assert get_coin_combination(coin) == expected
