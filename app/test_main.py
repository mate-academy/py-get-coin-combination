import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, expected",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should equal 1 penny"),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should equal 1 penny and 1 nickel"),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should equal 2 pennies, 1 nickel, 1 dime"),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should equal 2 quarters"),
        pytest.param(
            67,
            [2, 1, 1, 2],
            id="should2 equal 2 pennies, 1 nickel, 1 dime, 2 quarters")
    ]
)
def test_get_coin_combination(coins, expected):
    assert get_coin_combination(coins) == expected
