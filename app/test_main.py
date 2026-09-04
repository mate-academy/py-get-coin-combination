import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (68, [3, 1, 1, 2]),
        (119, [4, 1, 1, 4]),
    ]
)
def test_get_coin_combination_valid_inputs(
    cents: int,
    expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        "10",
        [10],
        {"cents": 10},
        None,
    ]
)
def test_get_coin_combination_incorrect_types(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
