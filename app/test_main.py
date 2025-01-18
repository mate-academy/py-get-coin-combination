from app.main import get_coin_combination
import pytest


def test_should_return_list():
    assert isinstance(get_coin_combination(1), list)


def test_function_should_return_list_size_4():
    assert len(get_coin_combination(1)) == 4


@pytest.mark.parametrize(
    "coins, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_result(coins: int, result: list):
    get_coin_combination(coins) == result
