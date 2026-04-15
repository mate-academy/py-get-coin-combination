import pytest
from app.combination import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (24, [4, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
])
def test_get_coin_combination_examples(
        cents: int,
        expected: list[int]
) -> None:
    res = get_coin_combination(cents)
    assert isinstance(res, list)
    assert len(res) == 4
    assert res == expected


def test_value_sum_matches_amount() -> None:
    for cents in [0, 4, 5, 9, 10, 24, 25, 49, 99]:
        coins = get_coin_combination(cents)
        total = coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25
        assert total == cents
