import pytest

from app.coin_combination import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="no money"
        ),
        pytest.param(
            2,
            [2, 0, 0, 0],
            id="just a penny"
        ),
        pytest.param(
            7,
            [2, 1, 0, 0],
            id="penny and nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="penny, nickel and dime"
        ),
        pytest.param(
            67,
            [2, 1, 1, 2],
            id="penny, nickel, dime and quarters"
        ),
    ]
)
def test_results(cents, coins):
    assert get_coin_combination(cents) == coins
