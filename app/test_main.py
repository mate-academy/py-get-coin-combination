import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        (1, [1, 0, 0, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 penny",
        "2 quarters"
    ]
)
def test_check_one_type(coins: int, result: list[int]) -> None:
    assert get_coin_combination(coins) == result


@pytest.mark.parametrize(
    "coins,result",
    [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0])
    ],
    ids=[
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime"
    ]
)
def test_check_multiple_types_at_same_time(
        coins: int, result: list[int]
) -> None:
    assert get_coin_combination(coins) == result
