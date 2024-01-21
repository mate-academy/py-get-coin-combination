from typing import Any
from app.main import get_coin_combination


# write your tests here
import pytest


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (69, [4, 1, 1, 2]),
        (74, [4, 0, 2, 2]),
    ]
)
def test_can_get_coin_combination(cents: int, result: int) -> None:
    assert (
        get_coin_combination(cents) == result
    ), (f"Coin combination of {cents} should be equal to {result}, "
        f"not {get_coin_combination(cents)}")


@pytest.mark.parametrize(
    "cents,result",
    [
        ("1", TypeError),
        ([], TypeError),
        ([3], TypeError),
        ({4}, TypeError),
        (None, TypeError),
    ]
)
def test_can_get_coin_combination_invalid_type(
        cents: Any,
        result: Any) -> None:
    with pytest.raises(result):
        get_coin_combination(cents)
