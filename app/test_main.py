import pytest


from app.main import get_coin_combination

def test_prefers_quarters_over_smaller_coins():
    assert get_coin_combination(50) == [0, 0, 0, 2]

def test_prefers_dimes_over_nickels():
    assert get_coin_combination(10) == [0, 0, 1, 0]

def test_prefers_nickels_over_pennies():
    assert get_coin_combination(5) == [0, 1, 0, 0]

@pytest.mark.parametrize("cents, expected", [
    (1,   [1, 0, 0, 0]),
    (6,   [1, 1, 0, 0]),
    (17,  [2, 1, 1, 0]),
    (50,  [0, 0, 0, 2]),
])
def test_spec_examples(cents, expected):
    assert get_coin_combination(cents) == expected