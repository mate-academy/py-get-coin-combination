from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),    # Testing with 1 cent
    (6, [1, 1, 0, 0]),    # Testing with 6 cents
    (17, [2, 1, 1, 0]),   # Testing with 17 cents
    (50, [0, 0, 0, 2]),   # Testing with 50 cents
    (0, [0, 0, 0, 0]),    # Testing with 0 cents
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    (3, [3, 0, 0, 0]),    # Testing with 3 cents (all pennies)
    (5, [0, 1, 0, 0]),    # Testing with 5 cents (1 nickel)
    (10, [0, 0, 1, 0]),   # Testing with 10 cents (1 dime)
    (25, [0, 0, 0, 1]),   # Testing with 25 cents (1 quarter)
    (37, [2, 0, 1, 1]),   # Testing with 37 cents (2
                          # pennies + 1 dime + 1 quarter)
])
def test_get_coin_combination_various(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        {3.5, 4},   # Testing with float value
        "10",       # Testing with string value
        [0, 1, 3],  # Testing with boolean value
        None
    ])
def test_get_coin_combination_invalid_input(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
