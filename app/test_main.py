import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (1000, [0, 0, 0, 40])
    ],
    ids=[
        "zero cents",
        "1 cent",
        "5 cents - 1 penny",
        "6 cents - 1 penny + 1 nickel",
        "10 cents - 1 dime",
        "11 cents - 1 dime + 1 penny",
        "16 cents - 1 dime + 1 nickel + 1 penny",
        "25 cents - 1 quarter",
        "26 cents - 1 quarter + 1 penny",
        "41 cents - 1 quarter + 1 dime + 1 nickel + 1 penny",
        "1000 cents - 40 quarters"
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"Coin combination from {cents} cents should be equal to {result}"


def test_cannot_use_str_as_cents() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents="50")
