import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (17, [2, 1, 1, 0]),
        (0, [0, 0, 0, 0]),
        (92, [2, 1, 1, 3]),
        (1, [1, 0, 0, 0]),
        (75, [0, 0, 0, 3]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (44, [4, 1, 1, 1]),
        (25, [0, 0, 0, 1]),
        (5, [0, 1, 0, 0]),
        (56, [1, 1, 0, 2]),
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected
