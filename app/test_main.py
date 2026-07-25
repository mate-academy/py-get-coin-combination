import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),

        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),

        (1234, None),
    ]
)
def test_get_coin_combination(
    cents: int, expected: list[int] | None
) -> None:
    result = get_coin_combination(cents)
    if expected is not None:
        assert result == expected
    else:
        total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
        assert total == cents


def test_non_negative_and_total() -> None:
    for cents in [0, 1, 2, 5, 7, 10, 23, 50, 99, 100, 500]:
        coins = get_coin_combination(cents)
        total = coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25
        assert total == cents
        assert all(x >= 0 for x in coins)
