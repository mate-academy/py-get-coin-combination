import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (34, [4, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (51, [1, 0, 0, 2]),
        (114, [4, 0, 1, 4]),
    ]
)
def test_coins(cents: int, coins: list[int]) -> None:
    assert get_coin_combination(cents) == coins


def test_negative_cents() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


@pytest.mark.parametrize(
    "cents",
    [
        15.5,
        True,
        "23",
        [24],
        (23,),
        {"cents": 24},
        {23}
    ],
    ids=[
        "float is invalid",
        "bool is invalid",
        "str is invalid",
        "list is invalid",
        "tuple is invalid",
        "dict is invalid",
        "set is invalid"
    ]
)
def test_invalid_input(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
