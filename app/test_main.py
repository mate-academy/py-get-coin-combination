import pytest

from app import main


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
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero_cents",
        "single_penny",
        "max_pennies_before_nickel",
        "single_nickel",
        "penny_and_nickel",
        "max_pennies_before_dime",
        "single_dime",
        "mixed_pennies_nickel_dime",
        "max_dimes_before_quarter",
        "single_quarter",
        "multiple_quarters",
        "large_value_all_coins",
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected


def test_result_length_should_always_be_four() -> None:
    result = main.get_coin_combination(63)
    assert len(result) == 4


def test_sum_of_coins_should_equal_cents() -> None:
    values = [1, 5, 10, 25]
    cents = 87
    result = main.get_coin_combination(cents)
    total = sum(count * value for count, value in zip(result, values))
    assert total == cents


def test_should_return_minimum_number_of_coins() -> None:
    result = main.get_coin_combination(30)
    assert sum(result) == 2
