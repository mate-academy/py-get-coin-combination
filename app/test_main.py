from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
