from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (42, [2, 1, 1, 1]),
        (57, [2, 1, 0, 2])
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
