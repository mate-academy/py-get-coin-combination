from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected",[
        (-5, [0, 0, 2, -1]),
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (86, [1, 0, 1, 3]),
        (333, [3, 1, 0, 13])
])

def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
