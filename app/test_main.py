import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_input, expected_output",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
        (0, [0, 0, 0, 0]),
        (25, [0, 0, 0, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(cents_input: int, expected_output: int) -> None:
    assert get_coin_combination(cents_input) == expected_output
