import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, coins",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="correct amount of pennies"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="correct amount of nickels"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="correct amount of dimes"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="correct amount of quarters"
        )
    ]
)
def test_get_coin_combination(
        cent: int,
        coins: list
) -> None:
    assert (
        get_coin_combination(cent) == coins
    )
