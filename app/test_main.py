from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        (
            1,
            [1, 0, 0, 0]
        ),

        (
            6,
            [1, 1, 0, 0]
        ),

        (
            17,
            [2, 1, 1, 0]
        ),

        (
            57,
            [2, 1, 0, 2]
        )
    ]
)
def test_get_coin_combination(input_value: int, expected_value: list) -> None:
    assert get_coin_combination(input_value) == expected_value
