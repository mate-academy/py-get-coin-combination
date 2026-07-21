from typing import Any
import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (1000, [0, 0, 0, 40]),
    ],
)
def test_get_coin_combination_valid_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "invalid_cents",
    [
        (-1),
        (-5),
        (-100),
    ],
)
def test_get_coin_combination_negative_cents(invalid_cents: int) -> None:
    assert get_coin_combination(invalid_cents) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "wrong_cents",
    [
        "15",
        15.5,
        None,
        True,
        False,
    ],
)
def test_get_coin_combination_invalid_types(wrong_cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(wrong_cents)
