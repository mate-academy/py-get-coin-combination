from typing import List

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("test_input, expected",
                         [
                             (1, [1, 0, 0, 0]),
                             (6, [1, 1, 0, 0]),
                             (17, [2, 1, 1, 0]),
                             (50, [0, 0, 0, 2])
                         ]
                         )
def test_get_coin_combination(test_input: int, expected: List[int]) -> None:
    assert expected == get_coin_combination(test_input)
