import pytest

from app.main import get_coin_combination


def test_returns_list() -> None:
    assert (
        isinstance(get_coin_combination(0), list)
    ), "Function should return a list"


def test_returns_four_item_list() -> None:
    assert (
        len(get_coin_combination(0)) == 4
    ), "Function should return a 4 items list"


@pytest.mark.parametrize(
    "cents, result",
    [
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ],
    ids=[
        "returns a nickel",
        "returns a dime",
        "returns a quarter"
    ]
)
def test_return_not_only_pennies(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"Function should return {result} when got {cents} as input"


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "0 cents",
        "1 cent",
        "6 cents",
        "17 cents",
        "24 cents",
        "50 cents"
    ]
)
def test_return_correct_values(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"{cents} cents as an input should return {result}"
