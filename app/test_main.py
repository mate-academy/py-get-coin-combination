from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "test expected result for 0 cents",
        "test expected result for 1 cents",
        "test expected result for 4 cents",
        "test expected result for 5 cents",
        "test expected result for 9 cents",
        "test expected result for 10 cents",
        "test expected result for 24 cents",
        "test expected result for 25 cents",
        "test expected result for 30 cents",
        "test expected result for 41 cents",
        "test expected result for 99 cents",
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        -1,
        -100,
    ],
    ids=[
        "negative 1 should raise an exception",
        "negative 100 should raise an exception",
    ]
)
def test_get_coin_combination_negative(cents: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    [
        "100",
        None,
        10.5,
        [],
        {},
    ],
    ids=[
        "wrong type input string",
        "wrong type input none",
        "wrong type input float",
        "wrong type input list",
        "wrong type input dict",
    ]
)
def test_get_coin_combination_invalid_types(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
