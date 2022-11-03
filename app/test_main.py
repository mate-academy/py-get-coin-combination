import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins_test",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_return_list_of_coins(cents: int,
                                     coins_test: list) -> None:

    coins = get_coin_combination(cents)

    assert coins == coins_test
