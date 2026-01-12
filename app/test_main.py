import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])

    ],
    ids=[
        "1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "2 quarters"
    ]
)
def test_all_cases(cents: int, coins: tuple[int, int, int, int]) -> None:
    assert (
        get_coin_combination(cents) == coins
    ), (f"{cents} Cents should return {coins[0]} pennies, "
        f" {coins[1]} nickels, {coins[2]} dims, {coins[3]} quarters")
