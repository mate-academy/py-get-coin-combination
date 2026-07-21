from app.main import get_coin_combination
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cents, coins",
    [
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3])
    ]
)
def test_collection_coins(
        cents: int,
        coins: list
) -> None:
    assert get_coin_combination(cents) == coins


@pytest.mark.parametrize(
    "cents, exception",
    [
        ({0: None}, TypeError),
        ("6", TypeError),
        ("int", TypeError),
        ({1, 2, 3}, TypeError)
    ]
)
def test_not_integer(
        cents: Any,
        exception: Exception
) -> None:
    with pytest.raises(exception):
        get_coin_combination(cents)
