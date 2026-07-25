import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, coins",
                         [pytest.param(0, [0, 0, 0, 0],
                                       id="test if zero cents"),
                          pytest.param(2, [2, 0, 0, 0],
                                       id="test pennies"),
                          pytest.param(7, [2, 1, 0, 0],
                                       id="test penny and nickel"),
                          pytest.param(17, [2, 1, 1, 0],
                                       id="test penny, nickel, dime"),
                          pytest.param(67, [2, 1, 1, 2],
                                       id="test all coins")])
def test_get_coin_combination(cents, coins):
    assert get_coin_combination(cents) == coins
