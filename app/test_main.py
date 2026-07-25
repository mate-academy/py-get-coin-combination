import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    pytest.param(1, [1, 0, 0, 0], id="Test the smallest input of 1 cent"),
    pytest.param(6, [1, 1, 0, 0],
                 id="Test input that requires both pennies and a nickel"),
    pytest.param(17, [2, 1, 1, 0],
                 id="Test input that requires pennies, a nickel, and a dime"),
    pytest.param(50, [0, 0, 0, 2], id="Test input that requires two quarters"),
    pytest.param(99, [4, 0, 2, 3], id="Test input just under a dollar"),
    pytest.param(100, [0, 0, 0, 4], id="Test input of exactly one dollar"),
    pytest.param(0, [0, 0, 0, 0], id="Test the edge case of 0 cents"),
    pytest.param(101, [1, 0, 0, 4], id="Test input just over a dollar"),
    pytest.param(11, [1, 0, 1, 0],
                 id="Test 11 cents to ensure correct dime and penny usage"),
    pytest.param(31, [1, 1, 0, 1],
                 id="Test 31 cents to check for quarter, nickel, penny use"),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
