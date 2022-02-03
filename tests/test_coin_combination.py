import pytest

from app.coin_combination import get_coin_combination


def test_get_penny():
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_get_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_dime():
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_get_quarter():
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_when_coin_is_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    'coin, expected',
    [
        (17, [2, 1, 1, 0]),
        (43, [3, 1, 1, 1]),
        (67, [2, 1, 1, 2]),
        (49, [4, 0, 2, 1])
    ]
)
def test_when_get_mix_or_all_coins(coin, expected):
    assert get_coin_combination(coin) == expected
