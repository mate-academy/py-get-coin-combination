import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (43, [3, 1, 1, 1]),
        (142, [2, 1, 1, 5])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
