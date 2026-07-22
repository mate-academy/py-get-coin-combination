from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents_amount, coins_combination",
    [
        pytest.param(1, [1, 0, 0, 0], id="should convert into 1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="should convert into 1 penny and 1 nickel"),
        pytest.param(16, [1, 1, 1, 0],
                     id="should convert into 1 penny, 1 nickel and 1 dime"),
        pytest.param(41, [1, 1, 1, 1],
                     id="should convert into 1 of each coin")
    ]
)
def test_should_return_different_coins(cents_amount: int,
                                       coins_combination: list) -> None:
    assert get_coin_combination(cents_amount) == coins_combination
