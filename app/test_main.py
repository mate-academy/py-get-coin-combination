import pytest

from app.main import get_coin_combination

get_coin_combination(1) == [1, 0, 0, 0]  # 1 penny
get_coin_combination(6) == [1, 1, 0, 0]  # 1 penny + 1 nickel
get_coin_combination(17) == [2, 1, 1, 0]   # 2 pennies + 1 nickel + 1 dime
get_coin_combination(50) == [0, 0, 0, 2]   # 2 quarters


@pytest.mark.parametrize(
    "cents,coins_set",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_coins_selected_correctly(cents: int,
                                  coins_set: list) -> None:
    assert (
        get_coin_combination(cents) == coins_set
    ), f"{cents} cents should be selected as {coins_set}."


@pytest.mark.parametrize(
    "cents",
    [
        ("1"),
        ([1, 1, 0, 0]),
        ({"cents": 100}),
        (tuple("aadfa")),
        (set("asdf"))
    ],
    ids=[
        "string",
        "list",
        "dict",
        "tuple",
        "set"
    ]
)
def test_cents_are_integer(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
