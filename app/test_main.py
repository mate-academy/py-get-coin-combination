import pytest
from app.main import get_coin_combination


test_data_valid = [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (4, [4, 0, 0, 0]),
    (9, [4, 1, 0, 0]),
    (24, [4, 0, 2, 0]),
    (41, [1, 1, 1, 1]),
    (99, [4, 0, 2, 3]),
    (123, [3, 0, 2, 4]),
    (200, [0, 0, 0, 8]),
]


@pytest.mark.parametrize("cents, expected", test_data_valid)
def test_get_coin_combination_valid_amounts(
        cents: int,
        expected: list
) -> None:

    assert get_coin_combination(cents) == expected
