import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),       # 1 penny
        (6, [1, 1, 0, 0]),       # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),      # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),      # 2 quarters
        (0, [0, 0, 0, 0]),       # 0 cents
        (4, [4, 0, 0, 0]),       # 4 pennies
        (5, [0, 1, 0, 0]),       # 1 nickel
        (10, [0, 0, 1, 0]),      # 1 dime
        (25, [0, 0, 0, 1]),      # 1 quarter
        (26, [1, 0, 0, 1]),      # 1 penny + 1 quarter
        (97, [2, 0, 2, 3]),      # 2 pennies + 0 nickels + 2 dimes + 3 quarters
        (100, [0, 0, 0, 4]),     # 4 quarters
    ],
    ids=[
        "1_penny",
        "1_penny_1_nickel",
        "2_pennies_1_nickel_1_dime",
        "2_quarters",
        "0_cents",
        "4_pennies",
        "1_nickel",
        "1_dime",
        "1_quarter",
        "1_penny_1_quarter",
        "2_pennies_0_nickels_2_dimes_3_quarters",
        "4_quarters",
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
