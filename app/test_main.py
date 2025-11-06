import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents: int, expected: list", [
    (0, [0, 0, 0, 0]),               # Brak monet
    (1, [1, 0, 0, 0]),               # 1 penny
    (4, [4, 0, 0, 0]),               # tylko pennies
    (5, [0, 1, 0, 0]),               # 1 nickel
    (6, [1, 1, 0, 0]),               # 1 penny + 1 nickel
    (10, [0, 0, 1, 0]),              # 1 dime
    (17, [2, 1, 1, 0]),              # 2 pennies + 1 nickel + 1 dime
    (25, [0, 0, 0, 1]),              # 1 quarter
    (30, [0, 1, 0, 1]),              # 1 quarter + 1 nickel
    (41, [1, 1, 1, 1]),              # 1 z każdej monety
    (49, [4, 0, 2, 1]),              # 1 quarter + 2 dimes + 4 pennies
    (50, [0, 0, 0, 2]),              # 2 quarters
    (99, [4, 0, 2, 3]),              # 3 quarters + 2 dimes + 4 pennies
    (100, [0, 0, 0, 4]),             # 4 quarters
    (123, [3, 0, 2, 4]),             # 4 quarters + 2 dimes + 3 pennies
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
