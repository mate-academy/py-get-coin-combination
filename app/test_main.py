import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_int,coins_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (8, [3, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (35, [0, 0, 1, 1]),
        (50, [0, 0, 0, 2]),
        (56, [1, 1, 0, 2]),
        (163, [3, 0, 1, 6]),
        (548, [3, 0, 2, 21]),
        (1892, [2, 1, 1, 75]),
        (747394, [4, 1, 1, 29895])

    ]
)
def test_get_coin_combination(
        cents_int: int,
        coins_list: list
) -> None:
    assert get_coin_combination(cents_int) == coins_list
