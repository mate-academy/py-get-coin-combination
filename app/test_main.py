import pytest
import app.main


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),  # zero cents
    (1, [1, 0, 0, 0]),  # 1 penny
    (4, [4, 0, 0, 0]),  # only pennies, boundary before nickel
    (5, [0, 1, 0, 0]),  # exactly 1 nickel
    (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
    (10, [0, 0, 1, 0]),  # exactly 1 dime
    (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
    (25, [0, 0, 0, 1]),  # exactly 1 quarter
    (50, [0, 0, 0, 2]),  # 2 quarters
    (99, [4, 0, 2, 3]),  # max single-dollar combination
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert app.main.get_coin_combination(cents) == expected
