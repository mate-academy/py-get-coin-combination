import pytest
import app.main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),            # Zero cents
        (1, [1, 0, 0, 0]),            # Only pennies
        (5, [0, 1, 0, 0]),            # Only nickels
        (6, [1, 1, 0, 0]),            # Pennies + nickels
        (10, [0, 0, 1, 0]),           # Only dimes
        (17, [2, 1, 1, 0]),           # Pennies + nickels + dimes
        (25, [0, 0, 0, 1]),           # Only quarters
        (50, [0, 0, 0, 2]),           # Multiple quarters
        (68, [3, 1, 1, 2]),           # 2 quarters, 1 dime, 1 nickel, 3 pennies
        (119, [4, 1, 1, 4]),          # 4 quarters, 1 dime, 1 nickel, 4 pennies
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert app.main.get_coin_combination(cents) == expected
