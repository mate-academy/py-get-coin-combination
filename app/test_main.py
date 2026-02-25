from app.main import get_coin_combination
import pytest


# write your tests here
@pytest.mark.parametrize(
    "coins, expected_result",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="with value 1 should return [1, 0, 0, 0] "
                        "where element index 0 is 1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="with value 6 should return [1, 1, 0, 0] "
                        "where element index is 1 penny and index 1 is "
                        "1 nickel"),
        pytest.param(17, [2, 1, 1, 0],
                     id="with value 17 should return [2, 1, 1, 0] "
                        "where element index 0 is 2 penny,index 1 is "
                        "1 nickel and index 2 is 1 dime"),
        pytest.param(50, [0, 0, 0, 2],
                     id="with value 50 should return [0, 0, 0, 2] "
                        "where element index 3 is 2 quarters")
    ]
)
def test_get_coin_combination(coins: int, expected_result: list) -> None:
    assert get_coin_combination(coins) == expected_result, \
        "should return expected result"
