from app.main import get_coin_combination
import pytest
from typing import Any, List


@pytest.mark.parametrize(
    "cents, list_of_cents",
    [
        pytest.param(
            -1,
            [4, 0, 2, -1],
            id="negative cents - invalid input"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="zero cents – no coins"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="only 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="1 nickel and 1 penny"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="1 dime, 1 nickel, 2 pennies"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="2 quarters"
        ),
        pytest.param(
            99,
            [4, 0, 2, 3],
            id="99 cents – mixed coins"
        ),
    ]
)
def test_get_coin_combination(cents: int, list_of_cents: List[int]) -> None:
    assert get_coin_combination(cents) == list_of_cents


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        pytest.param(
            "5",
            TypeError,
            id="string input instead of int"
        ),
        pytest.param(
            None,
            TypeError,
            id="None input instead of int"
        ),
    ]
)
def test_get_coin_combination_invalid_types(
        cents: Any,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
