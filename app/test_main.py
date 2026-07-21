import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 penny",
        "1 nickel",
        "1 dime",
        "1 quarter",
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


def test_zero_coin() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
