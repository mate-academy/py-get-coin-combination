from app.main import get_coin_combination
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_coin_combinations(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected


def test_negative_raises_value_error() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-100)


@pytest.mark.parametrize("bad_type", [1.5, "10", None, [], {}])
def test_bad_types_raise_type_error(bad_type: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(bad_type)


def test_large_value_performance_and_correctness() -> None:
    cents = 10**6
    result = get_coin_combination(cents)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) and x >= 0 for x in result)
    total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    assert total == cents


def test_mixed_coins_for_6_and_17() -> None:
    assert get_coin_combination(6)[0] > 0 and get_coin_combination(6)[1] > 0
    assert sum(1 for x in get_coin_combination(17) if x > 0) >= 2


def test_combination_for_30() -> None:
    coins = get_coin_combination(30)
    assert coins[3] == 1 and coins[1] == 1


def test_mixed_coins_examples() -> None:
    assert sum(1 for x in get_coin_combination(6) if x > 0) > 1
    assert sum(1 for x in get_coin_combination(17) if x > 0) > 1
    coins_30 = get_coin_combination(30)
    assert coins_30[3] > 0 and coins_30[1] > 0


@pytest.mark.parametrize("cents", [6, 17, 30, 41])
def test_returns_multiple_coin_types_for_some_values(cents) -> None:
    coins = get_coin_combination(cents)
    assert sum(1 for x in coins if x > 0) >= 2


def test_mixed_coin_examples():
    assert sum(1 for x in get_coin_combination(6) if x > 0) >= 2
    assert sum(1 for x in get_coin_combination(17) if x > 0) >= 2
    coins_30 = get_coin_combination(30)
    assert coins_30[3] > 0 and coins_30[1] > 0
