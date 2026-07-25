import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "sum_coins, specific_amount_in_cents",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_check(sum_coins: int, specific_amount_in_cents: int) -> None:
    assert get_coin_combination(sum_coins) == specific_amount_in_cents
