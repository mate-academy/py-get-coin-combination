import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3])
    ]
)
def test_get_coin_combinations(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_sum_matches_input() -> None:
    for cents in range(0, 100):
        coins = get_coin_combination(cents)
        total = coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25
        assert total == cents
