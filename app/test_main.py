import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),         # No coins
        (1, [1, 0, 0, 0]),         # 1 penny
        (5, [0, 1, 0, 0]),         # 1 nickel
        (10, [0, 0, 1, 0]),        # 1 dime
        (25, [0, 0, 0, 1]),        # 1 quarter
        (6, [1, 1, 0, 0]),         # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),        # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),        # 2 quarters
        (41, [1, 1, 1, 1]),        # 1 penny + 1 nickel + 1 dime + 1 quarter
        (99, [4, 0, 2, 3]),        # 4 pennies + 2 dimes + 3 quarters
    ],
    ids=[
        "0 cents (no coins)",
        "1 cent (1 penny)",
        "5 cents (1 nickel)",
        "10 cents (1 dime)",
        "25 cents (1 quarter)",
        "6 cents (penny + nickel)",
        "17 cents (pennies + nickel + dime)",
        "50 cents (2 quarters)",
        "41 cents (penny + nickel + dime + quarter)",
        "99 cents (4 pennies + 2 dimes + 3 quarters)",
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
