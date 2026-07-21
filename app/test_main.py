import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, output_list",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(coins: int, output_list: list) -> None:
    assert get_coin_combination(coins) == output_list
