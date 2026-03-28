import pytest
from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "initial_value, expected_value",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="1 penny + 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="2 penny + 1 nickel + 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="2 quarters"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="1 nickel"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="1 dime"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="1 quarter"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should handle zero input"
        ),
        pytest.param(
            322,
            [2, 0, 2, 12],
            id="should handle large input"
        ),
    ]
)
def test_function_works_correctly(
        initial_value: int,
        expected_value: list[int]
) -> None:
    assert get_coin_combination(initial_value) == expected_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        pytest.param(
            "36",
            id="string input"
        ),
        pytest.param(
            None,
            id="None input"
        ),
        pytest.param(
            [10],
            id="list input"
        )
    ]
)
def test_raises_type_error_for_invalid_input(invalid_value: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(invalid_value)
