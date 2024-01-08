import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),

    ],
    ids=[
        "for 0 cents",
        "for 1 cent",
        "for 6 cents",
        "for 17 cents",
        "for 50 cents",
        "for 99 cents",

    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    coins = get_coin_combination(cents)
    assert (
        coins == result
    ), f"{cents} should be equal {result}"
