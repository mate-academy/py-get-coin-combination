import pytest
from app import main


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (7, [2, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (41, [1, 1, 1, 1]),
        (42, [2, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (117, [2, 1, 1, 4]),
    ]
)
def test_get_coin_combination(cents: int, expected_coins: list) -> None:
    assert main.get_coin_combination(cents) == expected_coins
