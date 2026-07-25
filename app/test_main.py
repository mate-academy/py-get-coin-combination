import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,list_coins",
    [
        pytest.param(25, [0, 0, 0, 1], id="number of quarters"),
        pytest.param(19, [4, 1, 1, 0], id="number of dimes"),
        pytest.param(9, [4, 1, 0, 0], id="number of nickels"),
        pytest.param(4, [4, 0, 0, 0], id="number of pennies")
    ]
)
def test_number_of_coins(cents: int, list_coins: list) -> None:
    assert get_coin_combination(cents) == list_coins
