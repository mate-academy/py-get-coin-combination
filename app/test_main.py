import pytest
from typing import Any, List

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(
            67, [2, 1, 1, 2],
            id="Checking the correct operation of the function"
        )
    ]
)
def test_get_coin_combination(cents: int, result: List[int]) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents",
    [
        "2",
        (1, 2, 3),
        {1: 20},
        {23},
    ]
)
def test_raise_with_invalid_parameter(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents), (
            "Should raise TypeError"
        )
