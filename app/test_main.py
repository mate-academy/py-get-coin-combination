import pytest
from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),

        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),

        (6, [1, 1, 0, 0]),

        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),

        (17, [2, 1, 1, 0]),

        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),

        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (9999, [4, 0, 2, 399])
    ]
)
def test_returns_a_proper_list_for_int(cents: int, coins: list[int]) -> None:
    assert get_coin_combination(cents=cents) == coins


@pytest.mark.parametrize(
    "cents,coins",
    [
        (0.9, [0, 0, 0, 0]),
        (1.2, [1, 0, 0, 0]),
        (6.5, [1, 1, 0, 0]),
        (17.1, [2, 1, 1, 0]),
        (41.7, [1, 1, 1, 1]),
        (50.3, [0, 0, 0, 2])
    ]
)
def test_returns_a_proper_list_for_float(cents: int, coins: list[int]) -> None:
    assert get_coin_combination(cents=cents) == coins


@pytest.mark.parametrize(
    "cents",
    [
        "26",
        (4, 8, 15),
        [7, 3],
        {"cents": 26},
        {5, 3, 8}
    ]
)
def test_gives_error_for_invalid_cents_value(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents=cents)
