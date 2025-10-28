import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(coins: int, expected: list[int]) -> None:
    assert get_coin_combination(coins) == expected


@pytest.mark.parametrize(
    "bad_value",
    [
        10.0,
        "10",
        None,
        [10],
        {"coins": 10}
    ]
)
def test_get_coin_combination_bad_value(bad_value: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(bad_value)
