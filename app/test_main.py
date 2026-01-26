import pytest
from typing import List, Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
 
        (0, [0, 0, 0, 0]),

        (4, [4, 0, 0, 0]),


        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),


        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),


        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),


        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [-1, -5, -100])
def test_negative_input(cents: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize("cents", ["10", None, 5.5, [], {}])
def test_invalid_input_type(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
