import pytest
from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (31, [1, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (116, [1, 1, 1, 4])
    ],
    ids=[
        "0 cents value should return [0, 0, 0, 0]",
        "1 cents value should return [1, 0, 0, 0]",
        "5 cents value should return [0, 1, 0, 0]",
        "6 cents value should return [1, 1, 0, 0]",
        "10 cents value should return [0, 0, 1, 0]",
        "11 cents value should return [1, 0, 1, 0]",
        "15 cents value should return [0, 1, 1, 0]",
        "16 cents value should return [1, 1, 1, 0]",
        "25 cents value should return [0, 0, 0, 1]",
        "26 cents value should return [1, 0, 0, 1]",
        "31 cents value should return [1, 1, 0, 1]",
        "41 cents value should return [1, 1, 1, 1]",
        "116 cents value should return [1, 1, 1, 4]",
    ]
)
def test_get_coin_combination(cents: Any, expected: Any) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        -1
    ],
    ids=[
        "ValueError when cents is negative"
    ],
)
def test_should_raise_value_error_for_negative_cents(cents: Any) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    [
        None,
        1.5,
        "5",
        [0, None]
    ],
    ids=[
        "cents_none",
        "cents_float",
        "cents_string",
        "cents_list"
    ],
)
def test_should_raise_type_error_for_invalid_type(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
