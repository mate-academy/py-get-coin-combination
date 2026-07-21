import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        pytest.param(0, [0, 0, 0, 0], id="0 cents"),
        pytest.param(1, [1, 0, 0, 0], id="1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
        pytest.param(67, [2, 1, 1, 2], id="all coins")
    ]
)
def test_get_coin_combination(cents: int, expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins
