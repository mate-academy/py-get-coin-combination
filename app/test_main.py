import pytest
from app.main import get_coin_combination


def test_if_cents_0_should_be_zero_list() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_list_len_should_be_4() -> None:
    coins = get_coin_combination(25)
    assert len(coins) == 4


@pytest.mark.parametrize("cents, coins", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])
])
def test_should_return_coins_of_the_different_types(
        cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
