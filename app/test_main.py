import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coin_count_list",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_correctly_conversion_cents_into_coins(
        cents: int, coin_count_list: list[int]
) -> None:
    assert get_coin_combination(cents) == coin_count_list
