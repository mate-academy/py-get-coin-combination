from typing import List

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("number,expected", [
    pytest.param(1, [1, 0, 0, 0],
                 id="Given 1 number of pennies returns [1, 0, 0, 0]"),
    pytest.param(5, [0, 1, 0, 0],
                 id="Given 1 number of nickels returns [0, 1, 0, 0]"),
    pytest.param(10, [0, 0, 1, 0],
                 id="Given 1 number of dimes returns [0, 0, 1, 0]"),
    pytest.param(25, [0, 0, 0, 1],
                 id="Given 1 number of quarters returns [0, 0, 0, 1]"),
    pytest.param(41, [1, 1, 1, 1],
                 id="Given 41 returns [1, 1, 1, 1]"),

])
def test_get_coin_combination(number: int, expected: List[int]) -> None:
    assert get_coin_combination(number) == expected
