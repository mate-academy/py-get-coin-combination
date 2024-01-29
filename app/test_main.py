import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "penny",
        "nickel",
        "dime",
        "quarters"
    ]
)
def test_should_return_correct_combination_of_the_coins(
        cents: int,
        expected_combination: list
) -> None:
    assert (
        get_coin_combination(cents) == expected_combination
    ), "Should return the smallest possible combination of coins"
