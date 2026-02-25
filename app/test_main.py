import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent_count,exp_number_of_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (35, [0, 0, 1, 1]),
        (41, [1, 1, 1, 1]),
        (1010, [0, 0, 1, 40]),
    ]
)
def test_coin_combination(cent_count: int, exp_number_of_coins: int) -> None:
    assert get_coin_combination(cent_count) == exp_number_of_coins
