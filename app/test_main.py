from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents_int, cents_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (18, [3, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (52, [2, 0, 0, 2]),
    ],
)
def test_coin_combination(cents_int: int, cents_list: list[int]) -> None:
    assert get_coin_combination(cents_int) == cents_list
