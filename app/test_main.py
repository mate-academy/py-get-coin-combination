from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, par",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return only pennies"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return pennies and nickels"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return pennies, nickels and dimes"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return only quarters"
        ),
        pytest.param(
            947,
            [2, 0, 2, 37],
            id="shoul equal to result for a big number"
        )
    ]
)
def test_get_coin_combination(cents: int, par: list) -> None:
    assert get_coin_combination(cents) == par
