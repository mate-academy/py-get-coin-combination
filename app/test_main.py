import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),          # boundary: zero
        (1, [1, 0, 0, 0]),          # 1 penny
        (4, [4, 0, 0, 0]),          # only pennies
        (5, [0, 1, 0, 0]),          # single nickel
        (6, [1, 1, 0, 0]),          # penny + nickel
        (10, [0, 0, 1, 0]),         # single dime
        (17, [2, 1, 1, 0]),         # example from task
        (25, [0, 0, 0, 1]),         # single quarter
        (30, [0, 1, 0, 1]),         # quarter + nickel
        (41, [1, 1, 1, 1]),         # 25 + 10 + 5 + 1
        (50, [0, 0, 0, 2]),         # two quarters
        (99, [4, 0, 2, 3]),         # complex case
        (100, [0, 0, 0, 4]),        # four quarters
    ],
)
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected


def test_result_structure():
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4


def test_total_value_matches_input():
    cents = 73
    coins = get_coin_combination(cents)

    total = (
        coins[0] * 1 +
        coins[1] * 5 +
        coins[2] * 10 +
        coins[3] * 25
    )

    assert total == cents


def test_minimum_number_of_coins_property():
    # for US coin system greedy is optimal
    cents = 87
    coins = get_coin_combination(cents)

    total_coins = sum(coins)

    # Expected greedy solution manually calculated:
    # 87 = 3 quarters (75) + 1 dime (10) + 0 nickels + 2 pennies
    assert coins == [2, 0, 1, 3]
    assert total_coins == 6