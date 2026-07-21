import pytest
from typing import Type
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_return_correct_data(
        coins: int,
        result: list
) -> None:
    assert get_coin_combination(coins) == result


@pytest.mark.parametrize(
    "coins,expected_error",
    [
        ("8", TypeError),
        ([2, 4], TypeError),
        ({"coin": 34}, TypeError),
        ({2, 4}, TypeError)
    ]
)
def test_raising_errors(
        coins: int,
        expected_error: Type[BaseException]
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(coins)
