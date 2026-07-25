import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins_list",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_if_coins_combination_return_correct_amount(
        cents: int, coins_list: int
) -> None:
    assert get_coin_combination(cents) == coins_list, \
        ("should return a combination of the smallest possible "
         "number of coins, giving the same amount.")
