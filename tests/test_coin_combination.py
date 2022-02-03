import random

from app.coin_combination import get_coin_combination


def test_should_return_zeros_if_cents_equal_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_for_each_coin_in_list():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_return_right_result_for_default_value():
    cents = random.randint(42, 1000)
    res = get_coin_combination(cents)
    assert res[0] * 1 + res[1] * 5 + res[2] * 10 + res[3] * 25 == cents
