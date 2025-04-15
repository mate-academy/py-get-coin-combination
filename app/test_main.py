import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (10, [0, 0, 1, 0]),
        (30, [0, 1, 0, 1]),
        (75, [0, 0, 0, 3]),
        (99, [4, 0, 2, 3]),
        (24, [4, 0, 2, 0]),
        (26, [1, 0, 0, 1]),
    ],
)
def test_get_coin_combination(cents: int,
                              expected_result: [int]) -> None:
    assert get_coin_combination(cents) == expected_result
