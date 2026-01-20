from app.main import get_coin_combination
import pytest


# write your tests here
@pytest.mark.parametrize(
    "coin_value, coin_combo",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_coin_combination(coin_value: int, coin_combo: list) -> None:
    assert (get_coin_combination(coin_value) == coin_combo),\
        f"input is {coin_value} resulted in {coin_combo}"
