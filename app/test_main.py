import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (97, [2, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
    ids=[
        "1_penny",
        "2_quarters",
        "0_cents",
        "1_nickel",
        "1_dime",
        "1_quarter",
        "2_pennies_0_nickels_2_dimes_3_quarters",
        "4_quarters",
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
