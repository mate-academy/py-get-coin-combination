import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, number_of_coins", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])

    ]
)
def test_should_correctly_return_combination_of_coins(cents, number_of_coins):
    cents = cents
    assert get_coin_combination(cents) == number_of_coins
