import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (67, [2, 1, 1, 2])
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
