from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize("cents, expected", [
    pytest.param(1, [1, 0, 0, 0], id="1 penny"),
    pytest.param(4, [4, 0, 0, 0], id="4 penny"),
    pytest.param(6, [1, 1, 0, 0], id="1 penny + 1 nickel"),
    pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
    pytest.param(90, [0, 1, 1, 3], id="1 nickel + 1 dime + 3 quarters"),
    pytest.param(100, [0, 0, 0, 4], id="4 quarters")
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
