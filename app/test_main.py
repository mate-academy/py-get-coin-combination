from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    coins = get_coin_combination(cents)
    assert isinstance(coins, list), "повинно бути списком"
    assert len(coins) == 4, "довжина списку повинна бути 4"
    assert coins == expected
