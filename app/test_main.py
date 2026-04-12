import pytest
from typing import Any


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (68, [3, 1, 1, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_combination_valid_inputs(cents: int, expected: list) -> None:
    from app.main import get_coin_combination
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        "15",
        [15],
        None,
    ]
)
def test_get_coin_combination_wrong_types(cents: Any) -> None:
    from app.main import get_coin_combination
    with pytest.raises(TypeError):
        get_coin_combination(cents)
