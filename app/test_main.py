import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        pytest.param(
            2,
            [2, 0, 0, 0],
            id="only pennies"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="only nickels"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="only dimes"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="only quarters"
        ),
        pytest.param(
            67,
            [2, 1, 1, 2],
            id="returns a smallest combination"
        )
    ]
)
def test_get_coin_combination(coins, expected):
    assert get_coin_combination(coins) == expected
