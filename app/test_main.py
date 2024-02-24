import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("input_cents, expected_output", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (0, [0, 0, 0, 0]),
    (27, [2, 0, 0, 1]),
    (40, [0, 1, 1, 1]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (4, [4, 0, 0, 0]),
])
def test_get_coin_combination(
        input_cents: int,
        expected_output: list[int]) -> None:
    assert get_coin_combination(input_cents) == expected_output, \
        f"Failed for input: {input_cents}"
