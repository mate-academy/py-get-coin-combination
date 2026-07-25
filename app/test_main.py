import pytest
from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),

        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),

        (4, [4, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (24, [4, 0, 2, 0]),

        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),

        (41, [1, 1, 1, 1]),
        (68, [3, 1, 1, 2]),
        (119, [4, 1, 1, 4]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected
