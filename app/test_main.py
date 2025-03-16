import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,list_of_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_does_return_the_least_amount_of_coins(
    cents: int,
    list_of_coins: list[int]
) -> None:
    assert get_coin_combination(cents) == list_of_coins
