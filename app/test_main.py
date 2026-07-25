from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "value, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "only one cents",
        "6 cents",
        "17 cents",
        "50 cents"
    ]
)
def test_can_calculating_smallest_possible_coins(value: int,
                                                 result: list) -> None:
    assert (
        get_coin_combination(value) == result
    ), f"Coin combination from '{value}' should be equal '{result}'"
