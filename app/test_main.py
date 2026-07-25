from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cent,coin",
    [(1, [1, 0, 0, 0]),
     (6, [1, 1, 0, 0]),
     (17, [2, 1, 1, 0]),
     (50, [0, 0, 0, 2])]
)
def test_combination_of_the_smallest_possible_number_of_coins(
        cent: int,
        coin: list
) -> None:
    assert get_coin_combination(cent) == coin
