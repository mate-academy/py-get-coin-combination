import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, smallest_possible_number",
    [
        pytest.param(0, [0, 0, 0, 0], id="should return 0 for 0 cents"),
        pytest.param(1, [1, 0, 0, 0], id="should return 1 penny for 1 cents"),
        pytest.param(1, [1, 0, 0, 0], id="should return 1 penny for 1 cents"),
        pytest.param(6, [1, 1, 0, 0],
                     id="should return 1 penny, 1 nickel  for 6 cents"),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return 2 penny,2 nickel, 1 dime for 17 cents"),
        pytest.param(50, [0, 0, 0, 2],
                     id="should return 2 quarters  for 50 cents")
    ]
)
def test_should_get_coin_combination(
        cents: int,
        smallest_possible_number: list[int]
) -> None:
    assert get_coin_combination(cents) == smallest_possible_number


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param((1, 1, 1), id="Value should be an integer"),
        pytest.param("1", id="Value should be an integer"),
        pytest.param([1], id="Value should be an integer")
    ]
)
def test_should_raise_type_error(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
