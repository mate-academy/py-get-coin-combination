import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (50, [0, 0, 5, 2]),
        (99, [4, 0, 2, 3]),
        (123, [3, 4, 2, 4])
    ]
)
def test_right_return_for_given_number_of_coins(
        cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
