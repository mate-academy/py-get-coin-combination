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
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "zero",
        "one_penny",
        "only_pennies",
        "one_nickel",
        "nickel_plus_penny",
        "one_dime",
        "mixed_small",
        "one_quarter",
        "quarter_plus_nickel",
        "two_quarters",
        "complex_case",
    ],
)
def test_get_coin_combination_valid_cases(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected
