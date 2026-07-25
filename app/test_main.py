from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "amount, set_of_coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_correct_coin_combination(amount: int, set_of_coins: list) -> None:
    assert get_coin_combination(amount) == set_of_coins
