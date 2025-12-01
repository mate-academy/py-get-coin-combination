import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, values",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (60, [0, 0, 1, 2]),
        (115, [0, 1, 1, 4]),
        (117, [2, 1, 1, 4])
    ]
)
def test_get_coin_combination(coins: int, values: list[int]) -> None:
    assert get_coin_combination(coins) == values


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1", TypeError),
        ([1], TypeError)
    ]
)
def test_errors_get_coin_combination(value: str | list[int],
                                     expected: Exception) -> None:
    with pytest.raises(expected):
        get_coin_combination(value)
