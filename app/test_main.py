import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, ([0, 0, 0, 2]))
    ]
)
def test_get_coins_combination(cent: int, coins: list[int]) -> None:
    assert get_coin_combination(cent) == coins
