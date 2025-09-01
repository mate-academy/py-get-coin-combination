# tests/test_coin_combination.py


import pytest
from typing import List, Union, Any

from app.main import get_coin_combination


@pytest.mark.parametrize("cents,expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (9, [4, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (11, [1, 0, 1, 0]),
    (14, [4, 0, 1, 0]),
    (24, [4, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (26, [1, 0, 0, 1]),
    (29, [4, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (31, [1, 1, 0, 1]),
    (34, [4, 1, 0, 1]),
    (35, [0, 0, 1, 1]),
    (87, [2, 0, 1, 3]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (125, [0, 0, 0, 5]),
])
def test_get_coin_combination_various(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents,expected", [
    (-1, [4, 0, 2, -1]),
    (-25, [0, 0, 0, -1]),
])
def test_negative_inputs_return_greedy_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("bad", [
    "50",
    None,
    [100],
    (5,),
])
def test_invalid_types_raise_type_error(bad: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(bad)


@pytest.mark.parametrize("cents,expected", [
    (3.5, [3.0, 0.0, 0.0, 0.0]),
    (26.5, [1.0, 0.0, 0.0, 1.0]),
])
def test_float_inputs_return_float_counts(cents: Union[int, float], expected: List[float]) -> None:
    assert get_coin_combination(cents) == expected
