import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "zero_cents",
        "one_penny",
        "only_pennies",
        "one_nickel",
        "nickel_and_penny",
        "one_dime",
        "dime_nickel_and_pennies",
        "two_dimes_and_pennies",
        "one_quarter",
        "quarter_and_nickel",
        "all_coin_types",
        "two_quarters",
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
