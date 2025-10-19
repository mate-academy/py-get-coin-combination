import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 1])
    ]
)
def test_get_cion_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result
