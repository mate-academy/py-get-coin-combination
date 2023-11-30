import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (100, [0, 0, 0, 4]),
        (25, [0, 0, 0, 1]),
        (5, [0, 1, 0, 0]),
        (84, [4, 1, 0, 3]),
        (3278, [3, 0, 0, 131])

    ]
)
def test_can_get_coin_combination(coins: int, result: list) -> None:
    assert(
        get_coin_combination(coins) == result
    ), f"Function get_coin_combination should return" \
       f" {result} for {coins}"
