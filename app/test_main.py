from app import main
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (58, [3, 1, 0, 2]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (36, [1, 0, 1, 1])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected
