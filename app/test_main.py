from app.main import get_coin_combination


import pytest


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination_examples(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [0, 1, 6, 17, 41, 50, 99])
def test_get_coin_combination_represents_amount(cents: int) -> None:
    pennies, nickels, dimes, quarters = get_coin_combination(cents)
    assert pennies + nickels * 5 + dimes * 10 + quarters * 25 == cents
