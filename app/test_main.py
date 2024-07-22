import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (124, [4, 0, 2, 4])
    ]
)
def test_can_distribute_coins(cents: int, result_list: list[int]) -> None:
    assert get_coin_combination(cents) == result_list
