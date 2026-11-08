from typing import Any

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (99, [4, 0, 2, 3]),
        (1000, [0, 0, 0, 40]),
    ],
)
def test_get_coin_combination_valid_values(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    ["17", None, [17]],
)
def test_get_coin_combination_invalid_type_raises_type_error(
        cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
