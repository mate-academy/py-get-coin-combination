import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="return zeros if 0 cents",
        ),
        pytest.param(
            3, [3, 0, 0, 0],
            id="return only cents if < 5 cents",
        ),
        pytest.param(
            8, [3, 1, 0, 0],
            id="return cents and nickels if < 10 cents",
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="return dimes, cents and nickels if < 25 cents",
        ),
        pytest.param(
            58, [3, 1, 0, 2],
            id="return quarters, dimes, cents and nickels if > 25 cents",
        )
    ]
)
def test_coin_combination(
        cents: int,
        coins: list
) -> None:
    assert get_coin_combination(cents) == coins
