import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1])]
)
def test_boundaries(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
