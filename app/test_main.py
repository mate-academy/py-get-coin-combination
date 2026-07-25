import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents",
    [
        "cents",
        None,
        [1]
    ]
)
def test_should_raise_error_for_not_int(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        (1000, [0, 0, 0, 40]),
        (1546, [1, 0, 2, 61])
    ]
)
def test_should_give_correct_amount_of_coins(
        cents: int,
        result: list[int]
) -> None:
    assert (
        get_coin_combination(cents) == result
    ), "The calculation is wrong."
