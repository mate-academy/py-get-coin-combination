import pytest

from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        (124, [4, 0, 2, 4]),
        (1.5, [1.0, 0.0, 0.0, 0.0])
    ]
)
def test_should_return_correct_values(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        (-1, [4, 0, 2, -1]),
        (-6, [4, 1, 1, -1]),
        (-17, [3, 1, 0, -1]),
        (-50, [0, 0, 0, -2]),
        (-100, [0, 0, 0, -4]),
        (-124, [1, 0, 0, -5]),
    ]
)
def test_should_return_correct_values_for_invalid_cents(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,exception",
    [
        ("", TypeError),
        ([1], TypeError),
        ((1,), TypeError),
        ({1: 1}, TypeError),
        (None, TypeError),
    ]
)
def test_should_raise_error_for_invalid_cents(
        cents: Any,
        exception: Any
) -> None:
    with pytest.raises(exception):
        get_coin_combination(cents)
