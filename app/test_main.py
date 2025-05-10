import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount_of_coins, coin_parts",
    [
        pytest.param(1, [1, 0, 0, 0], id="Should return 1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="Should return 1 penny, 1 nickel"),
        pytest.param(17, [2, 1, 1, 0],
                     id="Should return 2 pennies, 1 nickel, 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="Should return 2 quarters"),
        pytest.param(41, [1, 1, 1, 1], id="Should return every type of parts"),
        pytest.param(0, [0, 0, 0, 0], id="Should return zeros in every parts")
    ]
)
def test_get_coin_combination(amount_of_coins: int, coin_parts: list[int]) -> None:
    assert (
        get_coin_combination(amount_of_coins) == coin_parts
    )
