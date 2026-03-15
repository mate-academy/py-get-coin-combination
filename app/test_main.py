import pytest
from app.main import get_coin_combination
from typing import Any


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination_values(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        "10",
        10.5,
        None,
        [10],
    ]
)
def test_get_coin_combination_raises_type_error(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
