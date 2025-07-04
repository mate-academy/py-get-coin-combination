import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),          # no money
    (1, [1, 0, 0, 0]),          # 1 penny
    (4, [4, 0, 0, 0]),          # only pennies
    (5, [0, 1, 0, 0]),          # 1 nickel
    (6, [1, 1, 0, 0]),          # 1 penny + 1 nickel
    (10, [0, 0, 1, 0]),         # 1 dime
    (11, [1, 0, 1, 0]),         # 1 penny + 1 dime
    (17, [2, 1, 1, 0]),         # 2 pennies + 1 nickel + 1 dime
    (25, [0, 0, 0, 1]),         # 1 quarter
    (30, [0, 1, 0, 1]),         # 1 nickel + 1 quarter
    (41, [1, 1, 1, 1]),         # 1 of each coin
    (50, [0, 0, 0, 2]),         # 2 quarters
    (99, [4, 0, 2, 3]),         # max value under 100
    (100, [0, 0, 0, 4]),        # 4 quarters (1 dollar)
])
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected


def test_large_value():
    # 1000 cents = $10
    result = get_coin_combination(1000)
    # Should be all in quarters: 1000 / 25 = 40
    assert result == [0, 0, 0, 40]


def test_type_and_length():
    result = get_coin_combination(87)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) and x >= 0 for x in result)
