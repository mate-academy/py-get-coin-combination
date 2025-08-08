from app.main import get_coin_combination
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (51, [1, 0, 0, 2]),
        (58, [3, 1, 0, 2]),
        (71, [1, 0, 2, 2])
    ]
)
def test_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,exception",
    [
        ({0: None}, TypeError),
        ("1", TypeError),
        ([1], TypeError),
        ({1, 3}, TypeError),
    ]
)
def test_exceptions_if_cents_not_integers(
        cents: Any,
        exception: Exception
) -> None:
    with pytest.raises(exception):
        get_coin_combination(cents)
