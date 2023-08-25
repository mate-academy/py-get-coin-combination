import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (25, [0, 0, 0, 1]),
        (63, [3, 0, 1, 2]),
        (118, [3, 1, 1, 4])
    ]
)
def test_get_coin_combination(cents: int, result: list):
    assert get_coin_combination(cents) == result
