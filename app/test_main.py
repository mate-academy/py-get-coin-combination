import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_coin_combinations(cents: int, expected: list[int]) -> None:
    result = get_coin_combination(cents)
    assert result == expected
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "invalid_input",
    [
        -1,
        -50,
        1.5,
        "25",
        None,
    ],
)
def test_invalid_inputs_raise_typeerror_or_valueerror(
    invalid_input: Any
) -> None:
    with pytest.raises(
        (ValueError, TypeError)
    ):
        get_coin_combination(invalid_input)
