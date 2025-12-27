import pytest

def get_coin_combination(cents):
    quarters, remainder = divmod(cents, 25)
    dimes, remainder = divmod(remainder, 10)
    nickels, pennies = divmod(remainder, 5)
    return [pennies, nickels, dimes, quarters]

@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (2, [2, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (75, [0, 0, 0, 3]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (123, [3, 0, 2, 4]),
    (249, [4, 0, 2, 9])
])
def test_get_coin_combination(cents, expected):
    result = get_coin_combination(cents)
    assert result == expected
    assert (result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25) == cents
