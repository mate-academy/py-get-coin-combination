import pytest
from app.main import get_coin_combination

@pytest.mark.parametrize(
    "coins,result",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="should return 1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="should return 1 penny, 1 nickel"),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return 2 pennies, 1 nickel, 1 dime"),
        pytest.param(50, [0, 0, 0, 2],
                     id="should return 2 quarters")
    ]
)
def test_coin_combination(
        coins: int,
        result: list
) -> None:
    assert get_coin_combination(coins) == result
