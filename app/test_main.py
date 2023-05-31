import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount,coins",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 coin have to return only 1 penny"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="5 coins have to return only 1 nickel"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="10 coins have to return only 1 dime"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="25 coins have to return only 1 quarter"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="current function must return all the types of coins"
        ),
    ]
)
def test_should_return_right_coin_count(
        amount: int,
        coins: [int, int, int, int]
) -> None:
    assert get_coin_combination(amount) == coins
