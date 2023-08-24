from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins, expected_result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="0 coins should convert to zeros")
        ,
        pytest.param(
            3,
            [3, 0, 0, 0],
            id="3 coins should convert to 3 cents"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="5 coins should convert to 1 nickel"
        ),
        pytest.param(
            11,
            [1, 0, 1, 0],
            id="11 coins should convert to 1 dime and 1 cent"
        ),
        pytest.param(
            33,
            [3, 1, 0, 1],
            id="33 coins should convert to 1 dime, 1 nickel and 3 cents"
        ),
    ]
)
def test_get_coin_combination(coins: int, expected_result: list) -> None:
    assert get_coin_combination(coins) == expected_result
