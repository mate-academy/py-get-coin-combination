import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (31, [1, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (36, [1, 0, 1, 1]),
        (41, [1, 1, 1, 1]),
        (999, [4, 0, 2, 39]),
    ]
)
def test_get_coin_combination(cents: int, expected_coins: list[int]) -> None:
    actual_coins = get_coin_combination(cents)
    assert actual_coins == expected_coins
