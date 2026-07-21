import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (-0, [0, 0, 0, 0]),   # -0 is 0
        (-6, [4, 1, 1, -1]),
        (-17, [3, 1, 0, -1]),
        (-50, [0, 0, 0, -2]),
    ],
)
def test_negative_values_for_get_coin_combination(cents: int,
                                                  expected: list[int]
                                                  ) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        None,
        "10",
    ],
)
def test_for_other_types_of_values(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
