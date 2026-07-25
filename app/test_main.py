import pytest

from app.main import get_coin_combination


# coins[0] = number of pennies (1 penny = 1 cent);
# coins[1] = number of nickels (1 nickel = 5 cents);
# coins[2] = number of dimes (1 dime = 10 cents);
# coins[3] = number of quarters (1 quarter = 25 cents).

@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (43, [3, 1, 1, 1]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
