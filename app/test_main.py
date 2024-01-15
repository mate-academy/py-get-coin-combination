import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,combination",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="1 penny and 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies, 1 nickel and 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
    ]
)
def test_coin_combinations(coins: int, combination: list) -> None:
    assert (
        get_coin_combination(coins) == combination
    ), f"Combination of {coins} coins should be equal to {combination}"
