import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_amount, coins_split",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_returns_correct_number_of_coins(
        cents_amount: int,
        coins_split: list
) -> None:
    assert get_coin_combination(cents_amount) == coins_split
