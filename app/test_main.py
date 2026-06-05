import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3])
    ]
)
def test_function_calculates_coin_combination_correctly(
    coins: int, result: list
) -> None:
    assert (get_coin_combination(coins) == result)


@pytest.mark.parametrize(
    "coins, result",
    [
        ("", TypeError),
        (None, TypeError),
    ]
)
def test_function_raise_errors_correctly(
    coins: int, result: list
) -> None:
    with pytest.raises(result):
        get_coin_combination(coins)
