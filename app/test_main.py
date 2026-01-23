import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),    # edge: 0 cents
        (1, [1, 0, 0, 0]),    # 1 penny
        (5, [0, 1, 0, 0]),    # 1 nickel
        (10, [0, 0, 1, 0]),   # 1 dime
        (25, [0, 0, 0, 1]),   # 1 quarter
        (6, [1, 1, 0, 0]),    # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),   # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),   # 2 quarters
        (99, [4, 0, 2, 3]),   # 3 quarters + 2 dimes + 4 pennies
        (100, [0, 0, 0, 4]),  # 4 quarters
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
