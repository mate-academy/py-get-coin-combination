import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_should_pick_proper_values_of_coins(cents: int, coins: list) -> None:
    assert (
        get_coin_combination(cents) == coins
    ), (
        f"{cents} cents equals {coins[0]} pennies, {coins[1]} nickels, "
        f"{coins[2]} dimes and {coins[3]} quaters."
    )
