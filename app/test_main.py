import pytest

from app.main import get_coin_combination


def test_get_coin_combination_should_return_list() -> None:
    assert isinstance(get_coin_combination(7), list)


@pytest.mark.parametrize(
    "cent, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "0 cent should be equal 0 coin",
        "1 cent should be 1 penny",
        "5 cent should be 1 nickel",
        "6 cent should be 1 penny + 1 nickel",
        "10 cent should be 1 dime",
        "17 cent should be 2 pennies + 1 nickel + 1 dime",
        "50 cent should be 2 quarters"
    ]
)
def test_functionality(cent: int, result: list[int]) -> None:
    assert get_coin_combination(cent) == result
