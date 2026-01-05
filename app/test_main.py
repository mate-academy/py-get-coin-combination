import pytest
from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(amount: int, expected: list[int]) -> None:
    assert get_coin_combination(amount) == expected


@pytest.mark.parametrize(
    "amount",
    [
        -1,
        -10,
        -50
    ]
)
def test_get_coin_combination_negative_amount(amount: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(amount)


@pytest.mark.parametrize(
    "amount",
    [
        1.5,
        7.8,
        "10",
        None,
        [25, 10]
    ]
)
def test_get_coin_combination_invalid_type(amount: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(amount)
