import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_number,number_of_coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(
        cents_number: int,
        number_of_coins: int
) -> None:

    assert get_coin_combination(cents_number) == number_of_coins
