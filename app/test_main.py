from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(0, [0, 0, 0, 0], id="0 penny for 0 cent"),
        pytest.param(1, [1, 0, 0, 0], id="penny for cent"),
        pytest.param(6, [1, 1, 0, 0], id="penny and nickel for 6 cents"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies, nickel and dime for 17 cents"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters for 50 cents"),
        pytest.param(41, [1, 1, 1, 1], id="penny, nickel, dime and quarter for 41 cents")
    ]
)
def test_get_coin_combination(
        cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result