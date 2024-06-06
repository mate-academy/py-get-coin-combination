from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (50, [0, 0, 0, 2]),
        (999, [4, 0, 2, 39])
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
# I don't understand why 2 tests are failing.
