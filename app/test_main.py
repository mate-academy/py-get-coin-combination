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
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1])
    ],
    ids=[
        "zero",
        "one_cent",
        "four_cents",
        "one_nickel",
        "one_nickel_one_cent",
        "one_dime",
        "one_quarter",
        "one_quarter_one_cent",
        "two_pennies_one_nickel_one_dime",
        "two_quarters",
        "all_types_cents"
    ]
)
def test_get_coin_combination(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected
