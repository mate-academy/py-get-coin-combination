from __future__ import annotations
import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "0 cents must return 0 penny",
        "1 cents must return 1 penny",
        "6 cents must return 1 penny + 1 nickel",
        "17 cents must return 2 pennies + 1 nickel + 1 dime",
        "50 cents must return 2 quarters"
    ]
)
def test_general(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents",
    [
        ("0"),
        ([0]),
        ({0}),
    ],
    ids=[
        "cents must be integer, not string",
        "cents must be integer, not list",
        "cents must be integer, not dict"
    ]
)
def test_correct_error_raise(cents: str | list | dict) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
