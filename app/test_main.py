import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, coins_quantity",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zeros"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 1 penny/nickel"
        ),
        pytest.param(
            16,
            [1, 1, 1, 0],
            id="should return 1 penny/nickel/daim"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return 1 penny/nickel/daim/quarter"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return 2 quarters"
        ),
    ]
)
def test_should_return_correct_quantity(
        coins: int, coins_quantity: list
) -> None:
    assert get_coin_combination(coins) == coins_quantity
