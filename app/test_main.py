import pytest

from app.main import get_coin_combination


coins_data = [
    (0, [0, 0, 0, 0]),  # 0 penny
    (1, [1, 0, 0, 0]),  # 1 penny
    (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
    (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
    (50, [0, 0, 0, 2]),  # 2 quarters
]


@pytest.mark.parametrize("coins,expectations", coins_data)
def test_coin_combination(coins: int, expectations: list[int]) -> None:
    assert get_coin_combination(coins) == expectations
