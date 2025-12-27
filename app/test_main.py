import pytest

def get_coin_combination(cents):
    quarters, cents = divmod(cents, 25)
    dimes, cents = divmod(cents, 10)
    nickels, pennies = divmod(cents, 5)
    return [pennies, nickels, dimes, quarters]

@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (41, [1, 1, 1, 1])
])
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected
