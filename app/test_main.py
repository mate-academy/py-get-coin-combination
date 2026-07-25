import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, combination_result",
    [
        (50, [0, 0, 0, 2]),
        (17, [2, 1, 1, 0]),
    ],
    ids=[
        "2 quaters",
        "2 pennies, 1 nickel, 1 dime"
    ]
)
def test_should_return_different_types_of_coins(
        cents: int,
        combination_result: list
) -> None:
    assert get_coin_combination(cents) == combination_result
