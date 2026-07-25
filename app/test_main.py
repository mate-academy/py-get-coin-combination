from typing import List, Any
import pytest
from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (43, [3, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination_valid(cents: int, expected: List[int]) -> None:
    assert main.get_coin_combination(cents) == expected


def test_cat_and_dog_different_inputs() -> None:
    assert main.get_coin_combination(5) == [0, 1, 0, 0]
    assert main.get_coin_combination(10) == [0, 0, 1, 0]
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


@pytest.mark.parametrize(
    "cents",
    [
        (-1),
        (-50),
    ],
)
def test_get_coin_combination_negative(cents: int) -> None:
    with pytest.raises(ValueError):
        main.get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    [
        ("10"),
        (10.5),
        (None),
        ([10]),
    ],
)
def test_get_coin_combination_invalid_types(cents: Any) -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination(cents)
