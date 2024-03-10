import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (37, [2, 0, 1, 1]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination(cents: int, expected_result: int) -> None:
    assert get_coin_combination(cents) == expected_result
