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
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero_cents",
        "one_penny",
        "four_pennies_max_before_nickel",
        "one_nickel",
        "penny_and_nickel",
        "four_pennies_and_nickel",
        "one_dime",
        "two_pennies_nickel_dime",
        "two_dimes_and_four_pennies",
        "one_quarter",
        "quarter_and_nickel",
        "quarter_two_dimes_four_pennies",
        "two_quarters",
        "three_quarters_two_dimes_four_pennies",
    ],
)
def test_get_coin_combination(
    cents: int,
    expected: list,
) -> None:
    assert get_coin_combination(cents) == expected
