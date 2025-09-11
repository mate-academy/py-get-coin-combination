import pytest
from typing import Any
from app.main import get_coin_combination


def test_get_coin_combination_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_pennies_only() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(2) == [2, 0, 0, 0]
    assert get_coin_combination(3) == [3, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_get_coin_combination_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(7) == [2, 1, 0, 0]
    assert get_coin_combination(8) == [3, 1, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_get_coin_combination_dimes() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(11) == [1, 0, 1, 0]
    assert get_coin_combination(15) == [0, 1, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_get_coin_combination_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(26) == [1, 0, 0, 1]
    assert get_coin_combination(30) == [0, 1, 0, 1]
    assert get_coin_combination(35) == [0, 0, 1, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_mixed_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]  # 1+5+10+25
    assert get_coin_combination(67) == [2, 1, 1, 2]  # 2+5+10+50
    assert get_coin_combination(99) == [4, 0, 2, 3]  # 4+0+20+75


def test_get_coin_combination_large_amounts() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]  # 4 quarters
    assert get_coin_combination(142) == [2, 1, 1, 5]  # 2+5+10+125
    assert get_coin_combination(87) == [2, 0, 1, 3]   # 2+0+10+75


def test_get_coin_combination_greedy_algorithm() -> None:
    # These test that quarters are maximized first
    assert get_coin_combination(31) == [1, 1, 0, 1]   # Not [6, 1, 0, 0]
    assert get_coin_combination(42) == [2, 1, 1, 1]   # Not [2, 3, 1, 1]
    # Test that dimes are used when beneficial
    assert get_coin_combination(16) == [1, 1, 1, 0]   # Not [1, 3, 0, 0]


def test_get_coin_combination_result_format() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(count, int) for count in result)
    assert all(count >= 0 for count in result)


def test_get_coin_combination_sum_verification() -> None:
    test_amounts = [0, 1, 13, 28, 49, 73, 88, 156]
    coin_values = [1, 5, 10, 25]

    for amount in test_amounts:
        coins = get_coin_combination(amount)
        total = sum(coins[i] * coin_values[i] for i in range(4))
        assert total == amount


@pytest.mark.parametrize("cents, error_type", [
    ("10", TypeError),
    (None, TypeError),
])
def test_get_coin_combination_invalid_inputs(
    cents: Any, error_type: type
) -> None:
    with pytest.raises(error_type):
        get_coin_combination(cents)


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (41, [1, 1, 1, 1]),
    (99, [4, 0, 2, 3]),
])
def test_get_coin_combination_examples(
    cents: int, expected: list[int]
) -> None:

    assert get_coin_combination(cents) == expected
