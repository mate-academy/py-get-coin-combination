import pytest

from app.main import get_coin_combination
from typing import List


@pytest.mark.parametrize(
    "cents, expected_combination",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="Should return all zeroes then number = 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="Should return one pennie then number = 1"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="Should return one pennie and one nickel then number = 6"
        ),
        pytest.param(
            16, [1, 1, 1, 0],
            id="Should return one pennie,"
               " one nickel and one dime then number = 16"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="Should return all ones then number = 41"
        ),
    ]

)
def test_combination_of_smallest_possible_number_of_coins(
        cents: int,
        expected_combination: List[int]) -> None:
    assert get_coin_combination(cents) == expected_combination
