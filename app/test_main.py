import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins_num,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (66, [1, 1, 1, 2])
    ]
)
def test_get_coin_combination(
        coins_num: int,
        result: list[int]
):
    assert get_coin_combination(coins_num) == result
