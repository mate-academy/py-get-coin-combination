import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,expected",
    [
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="4 coins equal 4 pennies"
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id="9 coins equal 4 pennies and 1 nickel"
        ),
        pytest.param(
            24,
            [4, 0, 2, 0],
            id="24 coins equal 4 pennies and 2 dimes"
        ),
        pytest.param(
            93,
            [3, 1, 1, 3],
            id="93 coins equal 3 pennies, 1 nickel, 1 dime and 3 quarters"
        )
    ]
)
def test_get_coin_combination(coins: int, expected: list) -> None:
    assert get_coin_combination(coins) == expected
