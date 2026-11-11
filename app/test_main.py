import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(0, [0, 0, 0, 0], id="0 cents returns no coins"),
        pytest.param(1, [1, 0, 0, 0], id="1 cent returns 1 penny"),
        pytest.param(5, [0, 1, 0, 0], id="5 cents returns 1 nickel"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents returns penny and nickel"),
        pytest.param(10, [0, 0, 1, 0], id="10 cents returns 1 dime"),
        pytest.param(
            17, [2, 1, 1, 0], id="17 cents returns pennies, nickel and dime"
        ),
        pytest.param(25, [0, 0, 0, 1], id="25 cents returns 1 quarter"),
        pytest.param(41, [1, 1, 1, 1], id="41 cents returns one of each coin"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents returns 2 quarters"),
        pytest.param(
            99, [4, 0, 2, 3], id="99 cents returns smallest number of coins"
        ),
    ]
)
def test_should_return_smallest_coin_combination(
        cents: int,
        coins: list
) -> None:
    assert get_coin_combination(cents) == coins
