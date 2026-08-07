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
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination_examples(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_returns_valid_coin_sum() -> None:
    for cents in range(0, 101):
        coins = get_coin_combination(cents)
        total = sum(coins[i] * value for i, value in enumerate((1, 5, 10, 25)))
        assert total == cents
        assert len(coins) == 4
        assert all(count >= 0 for count in coins)
