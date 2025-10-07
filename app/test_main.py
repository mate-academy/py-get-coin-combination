import pytest
from app.main import get_coin_combination


def test_returns_list_of_four_integers() -> None:
    result = get_coin_combination(2)
    assert len(result) == 4
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)


def test_zero_cents_returns_all_zeros() -> None:
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "value, expected",
    [(801, [1, 0, 0, 32]),
     (805, [0, 1, 0, 32]),
     (810, [0, 0, 1, 32]),
     (836, [1, 0, 1, 33]),
     ])
def test_large_value_distribution(value: int, expected: list) -> None:
    result = get_coin_combination(value)
    assert result == expected


@pytest.mark.parametrize("value", [6, 17, 50])
def test_sum_of_coins_equals_cents_property(value: int) -> None:
    result = get_coin_combination(value)
    assert sum([result[0] * 1,
                result[1] * 5,
                result[2] * 10,
                result[3] * 25]) == value
    assert all(x >= 0 for x in result)


@pytest.mark.parametrize(
    "value, expected",
    [(1, [1, 0, 0, 0]),
     (2, [2, 0, 0, 0])
     ])
def test_minimal_number_of_coins_property(value: int, expected: list) -> None:
    result = get_coin_combination(value)
    assert result == expected
