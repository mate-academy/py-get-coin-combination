import pytest
from typing import Any
from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (43, [3, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ]
)
def test_get_coin_combination_logic(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        "10",
        10.5,
        None,
        [10],
    ]
)
def test_get_coin_combination_invalid_types(cents: Any) -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination(cents)


def test_get_coin_combination_negative_values() -> None:
    assert main.get_coin_combination(-1) == [0, 0, 0, 0]
