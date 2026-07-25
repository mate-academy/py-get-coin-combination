from pytest import mark
from app.main import get_coin_combination


@mark.parametrize(
    "value, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "2 quarters",
    ]
)
def test_get_coin_combination(value: int, expected_result: list[int]) -> None:
    assert get_coin_combination(value) == expected_result
