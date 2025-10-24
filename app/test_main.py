import pytest
from typing import Any
from app.main import get_coin_combination


cases_single_coin = [
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
]

cases_mixed_coins = [
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (99, [4, 0, 2, 3]),
]

cases_edge_cases = [
    (0, [0, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (24, [4, 0, 2, 0]),
    (26, [1, 0, 0, 1]),
]

cases_invalid_type = [
    ("10",),
    (10.5,),
    (None,),
    ([10],),
]

cases_negative_type = [
    -1,
    -10,
]

cases_large_numbers = [
    (1000, [0, 0, 0, 40]),
    (1234, [4, 1, 0, 49]),
]

cases_boundary_values = [
    (9, [4, 1, 0, 0]),
    (19, [4, 1, 1, 0]),
    (49, [4, 0, 2, 1]),
]


@pytest.mark.parametrize("cents, expected", cases_single_coin)
def test_cases_single_coin(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", cases_mixed_coins)
def test_cases_mixed_coins(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", cases_edge_cases)
def test_cases_edge_cases(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", cases_invalid_type)
def test_cases_invalid_type(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)


@pytest.mark.parametrize("cents", cases_negative_type)
def test_cases_negative_type(cents: int) -> None:
    result = get_coin_combination(cents)
    assert all(x >= 0 for x in result)


@pytest.mark.parametrize("cents, expected", cases_large_numbers)
def test_cases_large_numbers(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", cases_boundary_values)
def test_cases_boundary_values(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
