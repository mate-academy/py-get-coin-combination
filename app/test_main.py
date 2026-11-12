import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (21, [1, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (31, [1, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (40, [0, 1, 1, 1]),
        (41, [1, 1, 1, 1]),
        (45, [0, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result
