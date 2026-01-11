import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, result", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (9, [4, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (24, [4, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (49, [4, 0, 2, 1]),
    (50, [0, 0, 0, 2]),
    (9999, [4, 0, 2, 399])
])
def test_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result
