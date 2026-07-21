import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected_coins", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
])
def test_get_coin_combination(
        cents: int,
        expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins
