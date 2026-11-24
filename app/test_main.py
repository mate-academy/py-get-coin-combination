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
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (999999, [4, 0, 2, 39999]),
        (1000000, [0, 0, 0, 40000]),
    ],
)
def test_should_return_smallest_number_of_coins(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [0, 1, 25, 1000000],
)
def test_should_return_list_of_four_coin_counts(cents: int) -> None:
    assert len(get_coin_combination(cents)) == 4


@pytest.mark.parametrize(
    "cents",
    ["10", None, [10]],
)
def test_should_raise_type_error_for_incorrect_types(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
