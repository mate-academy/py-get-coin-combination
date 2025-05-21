import pytest


from app.main import get_coin_combination


# write your tests here
@pytest.mark.parametrize(
    "coins,result_list",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="1 cent returns 1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="6 cents return 1 nickel and 1 penny"),
        pytest.param(10, [0, 0, 1, 0],
                     id="10 cents return 1 dime"),
        pytest.param(17, [2, 1, 1, 0],
                     id="17 cents return 1 dime 1 nickel and 2 pennies"),
        pytest.param(23, [3, 0, 2, 0],
                     id="23 cents return 2 dimes and 3 pennies"),
        pytest.param(50, [0, 0, 0, 2],
                     id="50 cents return 2 quarters"),
    ])
def test_get_coin_combination(coins: int, result_list: list[int]) -> None:
    result = get_coin_combination(coins)
    assert result == result_list