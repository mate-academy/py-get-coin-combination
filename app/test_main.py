import pytest
from app.main import get_coin_combination
from typing import Any


@pytest.mark.parametrize(
    "coins, combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_combination(
        coins: int,
        combination: list[int]
) -> None:
    assert get_coin_combination(coins) == combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            None,
            TypeError
        ),
        pytest.param(
            [],
            TypeError
        )
    ]
)
def test_errors(cents: Any, expected: Any) -> None:
    with pytest.raises(expected):
        get_coin_combination(cents)
