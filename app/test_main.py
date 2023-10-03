import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected_result", [
    (1, [1, 0, 0, 0]),  # 1 penny
    (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
    (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
    (50, [0, 0, 0, 2]),  # 2 quarters
    (0, [0, 0, 0, 0]),  # No coins
    (20, [0, 0, 2, 0]),  # 2 dimes
    (100, [0, 0, 0, 4]),  # 4 quarters
    (7, [2, 1, 0, 0]),  # 2 pennies + 1 nickel
    (99, [4, 0, 2, 3]),  # 4 pennies + 2 dimes + 3 quarters
    (11, [1, 0, 1, 0]),  # 1 penny + 1 dime
    (32, [2, 1, 0, 1]),  # 2 pennies + 1 nickel + 1 quarter
])
def test_get_coin_combination(cents, expected_result) -> None:
    assert get_coin_combination(cents) == expected_result
