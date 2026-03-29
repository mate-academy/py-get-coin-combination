import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="Should return zero coins if value is 0"
        ),
        pytest.param(
            4, [4, 0, 0, 0],
            id="Only pennies for values up to 5"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="Only nickel if value is 5"
        ),
        pytest.param(
            8, [3, 1, 0, 0],
            id="Only pennies and nickel for values up to 10"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="Only 1 dime if  value is 10"
        ),
        pytest.param(
            16, [1, 1, 1, 0],
            id="Only pennies, nickels and dimes for values up to 10"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="Only 1 quarter if  value is 25"
        ),
        pytest.param(
            117, [2, 1, 1, 4],
            id="For large values, all types of coins can be used"
        )
    ],
)
def test_coins_combination(coins: int, expected: bool) -> None:
    assert get_coin_combination(coins) == expected
