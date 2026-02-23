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
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_result_structure() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4


def test_total_value_matches_input() -> None:
    cents: int = 73
    coins: list[int] = get_coin_combination(cents)

    total = (
        coins[0] * 1
        + coins[1] * 5
        + coins[2] * 10
        + coins[3] * 25
    )

    assert total == cents


def test_minimum_number_of_coins_property() -> None:
    coins: list[int] = get_coin_combination(87)

    assert coins == [2, 0, 1, 3]
    assert sum(coins) == 6