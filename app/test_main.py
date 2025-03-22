from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, list_of_coins", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
])
def test_number_of_coins(cents: int, list_of_coins: list) -> None:
    result = get_coin_combination(cents)
    assert result == list_of_coins
# write your tests here
