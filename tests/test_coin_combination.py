import pytest
from app.main import get_coin_combination


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_basic_cases():
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_more_values():
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(30) == [0, 1, 0, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_sum_is_correct():
    for cents in range(0, 100):
        p, n, d, q = get_coin_combination(cents)
        total = p + n * 5 + d * 10 + q * 25
        assert total == cents


def test_minimum_coins():
    for cents in range(0, 100):
        result = get_coin_combination(cents)
        total_coins = sum(result)

        min_coins = float("inf")

        for q in range(cents // 25 + 1):
            for d in range((cents - q * 25) // 10 + 1):
                for n in range((cents - q * 25 - d * 10) // 5 + 1):
                    p = cents - q * 25 - d * 10 - n * 5
                    coins = p + n + d + q
                    if coins < min_coins:
                        min_coins = coins

        assert total_coins == min_coins
