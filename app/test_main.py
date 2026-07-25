from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins, result",
    [
        pytest.param(0, [0, 0, 0, 0],
                     id="Check if coin is 0"),
        pytest.param(1, [1, 0, 0, 0],
                     id="Check if coin is 1"),
        pytest.param(6, [1, 1, 0, 0],
                     id="Check if coin is 6"),
        pytest.param(17, [2, 1, 1, 0],
                     id="Check if coin is 17"),
        pytest.param(50, [0, 0, 0, 2],
                     id="Check if coin is 50")
    ]
)
def test_result(coins: int, result: list[int]) -> None:
    assert (
        get_coin_combination(coins) == result
    )
