from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_cents_converted_to_combination_of_smallest_coin(
        cents: int,
        expected_result: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_result
