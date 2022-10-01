import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin,expected_rezult",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 3])
    ]
)
def test_should_return_number_of_coins(coin, expected_rezult):
    assert get_coin_combination(coin) == expected_rezult, \
        "The function should return the combination of the smallest \
possible number of coins"
