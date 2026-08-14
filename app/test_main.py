import pytest

from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (31, [1, 1, 0, 1]),
        (36, [1, 0, 1, 1]),
        (41, [1, 1, 1, 1]),
        (78, [3, 0, 0, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected
